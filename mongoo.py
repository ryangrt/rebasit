#
# mongo Operations
#
import sys
from datetime import datetime
import config

#
# user:passwd@hostipaddr:port/database/collection
#
def parse_concol(s):
    ret = {}
    if '@' in s:
        up, s = s.split('@')
        if ':' in up:
            ret['user'], ret['password']  = up.split(':')
        else:
            ret['user'], ret['password'] = up, config.password
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
        ret['database'] = temp[0]
        ret['collection'] = temp[1] 
    else:
        raise Exception("parse_concol format: [user:passwd@][hostipaddr][:port]]/database/collection")
    return ret

#
# mongoo(concol1, [concol2, ...] cb, [qarg1=val1, ...])
# call with source connection/collection, dest concol, callback, args for mongoengine query
#
def mongoo(*args, **kw):
    print "mongoo args:", args
    print "mongoo kw:", kw

if __name__ == "__main__":
    if len(sys.argv) > 1:
        exec(sys.argv[1])
    else:
        mongoo ("local_db/goosrc", goosrc_do)