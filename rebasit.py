#!/usr/bin/python
#
# Clever little hack to squash all commits that are repeats of previous commit msg into one commit
#
import sys, os
PYBASE = os.path.abspath(os.path.dirname(__file__)) 
try:
    arg = sys.argv[1]
except:
    print "rebasit <commit>"
    print "#rebases squashing repeat comments"
    exit()

if "git-rebase-todo" in arg:
    #act as editor
    f = open(arg)
    o = []
    oldmsg = None
    for r in f.readlines():
        r = r.strip()
        if len(r) and r[:5] == 'pick ':
            r = r[5:]
            i = r.find(' ')
            commit = r[:i]
            message = r[i+1:]
            if message == oldmsg:
    #             print commit, "SQUASH"
                o.append("f %s %s" % (commit, message))
            else:
                o.append("pick %s %s" % (commit, message))
            print o[-1]
            oldmsg = message
    f.close()
    print "\nrebasit_edit done"
    
    f = open(arg, 'w')
    for r in o:
        f.write(r + "\n")
    f.close()
else:
    #invoke git rebase with me as editor
    os.environ['GIT_EDITOR'] = PYBASE + "/rebasit.py"
    cmd = "git rebase -i " + arg
    print cmd
    os.system(cmd)
