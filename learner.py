#! /usr/bin/env python
# coding=utf-8

import sys
print "Your terminal's encoding:", sys.stdout.encoding

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
cuff = Paradigm(u'kʌf', [(u'kʌvz', 0.1), (u'kʌfs', 0.9)])
reef = Paradigm('rif', [('rivz', 0.1), ('rifs', 0.9)])
giraffe = Paradigm(u'ʤɪɹæf', [(u'ʤɪɹæfs', 0.5), (u'ʤɪɹævz', 0.5)])
eighteenth = Paradigm(u'eɪtinθ', [(u'eɪtinθs', 0.8), (u'eɪtinðz', 0.2)])
waf = Wug('waf')

word_list = [knife, cuff, reef, giraffe, eighteenth]

for paradigm in word_list:
  derivs = map(lambda x: x.form, paradigm.derivatives)
  print "Analyzing word", paradigm.base.ipa_string()
  print "Faithfulness constraints:"
  for con in cons.faithfuls:
    print con.__name__
    for form in derivs:
      print form.ipa_string(), con(paradigm.base, form)
  print "Markedness constraints:"
  for con in cons.markeds:
    print con.__name__
    for form in derivs:
      print form.ipa_string(), con(form)

# We need to fix syllabification    
print [ map(lambda x: x.ipa, p) for p in knife.best_derivative().syllables()]
print knife.best_derivative().sonority()