
from lib.paradigm import *

def nw_test(str1, str2):
  paradigm = Paradigm(str1, str2)
  for form in paradigm.forms:
    map(lambda s: sys.stdout.write("%s has %s stress\n" % (s.segments, s.stress)), form)
