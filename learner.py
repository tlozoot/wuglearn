#! /usr/bin/python
# coding=utf8

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
waf = Wug('waf')

print map(lambda x: x.ipa_string(), map(add_z, map(lambda x: x.base, [knife, cuff, reef, waf])))