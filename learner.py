#! /usr/bin/env python
# coding=utf-8

import sys
# print "Your terminal's encoding:", sys.stdout.encoding

# See what this imports with help(lib)
from lib import *
from lib.paradigm import Paradigm
from lib.form import Form
from lib.wug import Wug
import lib.constraint as cons
import re

# Read in a file from somewhere in data-
# This part will change; we want to be pretty agnostic about how these things are formatted, at least for now
# Also, application-specific code will go here--for example, the rules about how plurals change

def add_s(form):
  return Form(form.ipa_string() + 's')
    
def add_z(form):
  return Form(re.sub('f$', 'vz', form.ipa_string()))
  
change_set = set([add_s, add_z])

knife = Paradigm('naif', [('naivz', 0.9), ('naifs', 0.1)])
leaf = Paradigm('lif', [('livz', 0.9), ('lifs', 0.1)])
cuff = Paradigm(u'kʌf', [(u'kʌvz', 0.1), (u'kʌfs', 0.9)])
reef = Paradigm('rif', [('rivz', 0.4), ('rifs', 0.6)])
giraffe = Paradigm(u'ʤɪɹæf', [(u'ʤɪɹæfs', 0.55), (u'ʤɪɹævz', 0.45)])
eighteenth = Paradigm(u'eɪtinθ', [(u'eɪtinθs', 0.8), (u'eɪtinðz', 0.2)])
waf = Wug('waf')

word_list = [leaf, reef, giraffe, cuff, eighteenth]

for con in cons.faithfuls:
  for paradigm in word_list:
    for derivative in paradigm.derivatives:
      for a in alignment.align_forms(paradigm.base, derivative.form):
        score = con.func(paradigm.base, derivative.form, a)
        con.scores[derivative.form.ipa_string()] = (score * derivative.probability)

for con in cons.markeds:
  for paradigm in word_list:
    for derivative in paradigm.derivatives:
      score = con.func(derivative.form)
      con.scores[derivative.form.ipa_string()] = (score * derivative.probability)

cons.print_table(word_list, cons.faithfuls, cons.markeds)

    