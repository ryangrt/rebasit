#
# mongo Operations
#
import sys
from datetime import datetime
import mongoengine as meng
from mongoengine.connection import get_db
from mongoengine import register_connection
from mongoengine.context_managers import switch_db

#
# user:passwd@hostipaddr:port/database/collection
#
def parse_concol(s):
    ret = {}
    if '@' in s:
        up, s = s.split('@')
        ret['user'], ret['password']  = up.split(':')
    else:
        ret['user'], ret['password']  = None, None
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

def open_concol(cc):
    cc = parse_concol(cc)
    meng.connect(cc['database'], host=cc['host'], port=cc['port'], username=cc['user'], password=cc['password'])
    return globals()[ cc['collection'] ]
#
# mongoo(concol1, [concol2, ...] cb, [qarg1=val1, ...])
# call with source connection/collection, dest concol, callback, args for mongoengine query
#
def mongoo(src, *args, **kw):
    src = open_concol(src)
#     print "source:", src
    cb = args[-1]
#     print "mongoo args:", args[:-1]
#     print "mongoo kw:", kw
    cb(src, *args[:-1], **kw)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        exec(sys.argv[1])
        exit()
    class parsed(meng.Document):
        pass
    def goosrc_cb(src, *args, **kw):
        print "goosrc_cb:", src, args, kw, src.objects.count()

    mongoo ("parsed", goosrc_cb, flaggy=1)
    mongoo ("127.0.0.1:27017/sci_testdb/parsed", goosrc_cb, flaggy=2)
