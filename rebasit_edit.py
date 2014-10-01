#!/usr/bin/python
#
# this editor is invoked by rebasit to fake out git
#
import sys, time

print sys.argv[1], "is what I would edit if so inclined. wait 4 it"

f = open(sys.argv[1])
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

f = open(sys.argv[1], 'w')
for r in o:
    f.write(r + "\n")
f.close()