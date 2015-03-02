#
# mongo Operations
#
import sys
from datetime import datetime

#
# user:passwd@hostipaddr:port/database/collection
#
def parse_concol(s):
    ret = {}
    if '@' in s:
        up, s = s.split('@')
        ret['user'], ret['password']  = up.split(':')
    if ':' in s:
        ret['host'], s = s.split(':')
    else:
        ret['host'] = "localhost"
    temp = s.split('/')
    if len(temp) == 3:
        ret['port'] = temp[0]
        ret['database'] = temp[1]
        ret['collection'] = temp[2] 
    elif len(temp) == 2:
        ret['port'] = 27017
        ret['database'] = temp[0]
        ret['collection'] = temp[1] 
    elif len(temp) == 1:
        ret['port'] = 27017
        ret['database'] = "local_db"
        ret['collection'] = temp[0] 
    else:
        raise Exception("parse_concol format: [user:passwd@][hostipaddr][:port]]/database/collection")
    return ret

#
# mongoo(concol1, [concol2, ...] cb, [qarg1=val1, ...])
# call with source connection/collection, dest concol, callback, args for mongoengine query
#
def mongoo(src, *args, **kw):
    src = parse_concol(src)
#     print "source:", src
    cb = args[-1]
#     print "mongoo args:", args[:-1]
#     print "mongoo kw:", kw
    cb(src, *args[:-1], **kw)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        exec(sys.argv[1])
        exit()
    def goosrc_cb(src, *args, **kw):
        print "goosrc_cb:", src, args, kw

    mongoo ("goosrc", goosrc_cb, flaggy=1)
