#!/usr/bin/python
#
# Clever little hack to squash all commits that are repeats of previous commit msg into one commit
#
import sys, os

os.environ['GIT_EDITOR'] = "./rebasit_edit.py"
cmd = "git rebase -i " + sys.argv[1]
print cmd
os.system(cmd)
