#! /usr/bin/env python
# coding=utf-8

import sys
print "Your terminal's encoding:", sys.stdout.encoding

# See what this imports with help(lib)
from lib import *
from lib.paradigm import Paradigm
from lib.form import Form
from lib.wug import Wug
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

word_list = [knife, cuff, reef, waf, giraffe, eighteenth]

# print map(lambda x: add_z(x.base).ipa_string(), word_list)
print alignment.align_forms_with_scores(knife.base, cuff.base)

print eighteenth.base.sonority()

print map(lambda x: map(lambda y: y.to_print(), x), eighteenth.base.syllables())

for c in list(giraffe.base.segments()):
  print c.to_print(),