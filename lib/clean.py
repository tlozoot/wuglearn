#! /usr/bin/env python

# Remove .pyc files. A fun excercise...

import sys
import os
import os.path
import re

def remove_pyc(cdir):
  for f in os.listdir(cdir):
    if re.search("\.pyc$", f):
      os.remove(os.path.join(cdir, f))
    elif os.path.isdir(f):
      remove_pyc(f)
      
if len(sys.argv) > 1:
  remove_pyc(sys.argv[1])
else:
  remove_pyc(os.getcwd())
