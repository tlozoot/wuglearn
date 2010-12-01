#! /usr/bin/env python
# coding=utf-8

import sys
import logging
import re

from lib import *
from lib.paradigm import Paradigm
from lib.form import Form
from lib.wug import Wug
import lib.constraint as cons

##### Change set ######

def voiceless_pl(form):
    return Form(form.to_u() + 's')
        
def voiced_pl(form):
    if form.segments()[-1].ipa == u'θ':
        return Form(re.sub(u'θ$', u'ðz', form.to_u()))
    else:
        return Form(re.sub('f$', 'vz', form.to_u()))
    
change_set = set([voiceless_pl, voiced_pl])

##### Read the words in ######

word_list = []
wug_list = []

# Read in the voiciness of every item, on the 1-7 scale
voiciness_dict = dict()
voiciness_lines = util.open_csv('plural_data/all_plural_voiciness.csv')
for line in voiciness_lines:
    _, word, voiciness = map(lambda x: x.strip(), line)
    voiciness_dict[str(word)] = float(voiciness)

# Get the IPA of each real word, and add the actual Paradigms to word_list
plural_ipa_lines = util.open_csv('plural_data/real_plurals.csv')
del(plural_ipa_lines[0])
for line in plural_ipa_lines:
    if line[7] == 'stim':
        ortho, ipa = line[0], unicode(line[1], 'utf8')
        voiciness = voiciness_dict[ortho]
        derivatives = []
        for change in change_set:
            derivative = change(Form(ipa))
            # This is a hack! Do something nicer later
            if change.__name__ == 'voiced_pl':
                score = (voiciness - 1) / 6
            else:
                score = 1 - ((voiciness - 1) / 6)
            derivatives.append((derivative, score))
        paradigm = Paradigm(ipa, derivatives, ortho=ortho)
        word_list.append(paradigm) 

# Get MinGen's voiciness scores
mingen_voiciness = dict()
mingen_lines = util.open_sep('plural_data/mingen_voiciness.txt', "\t")
del(mingen_lines[0])
for line in mingen_lines:
    word, voice = line[0], line[6]
    mingen_voiciness[word] = float(voice)

# Get the wugs!
wug_lines = util.open_csv('plural_data/wug_plurals.csv')
for line in wug_lines:
    if line[13] == 'stim':
        ortho, ipa = line[0], unicode(line[4], 'utf8')
        try:
            mingen_voice = mingen_voiciness[ortho]
        except KeyError: 
            mingen_voice = 0
        wug_list.append(Wug(ipa, change_set, ortho=ortho,
                            human_voiciness=voiciness_dict[ortho], 
                            mingen_voiciness=mingen_voice))

# # Sample data--for historical purposes... to be moved...
# knife = Paradigm('naif', [('naivz', 0.9), ('naifs', 0.1)])
# leaf = Paradigm('lif', [('livz', 0.9), ('lifs', 0.1)])
# cuff = Paradigm(u'kʌf', [(u'kʌvz', 0.1), (u'kʌfs', 0.9)])
# reef = Paradigm('rif', [('rivz', 0.4), ('rifs', 0.6)])
# giraffe = Paradigm(u'ʤɪɹæf', [(u'ʤɪɹæfs', 0.55), (u'ʤɪɹævz', 0.45)])
# eighteenth = Paradigm(u'eɪtinθ', [(u'eɪtinθs', 0.8), (u'eɪtinðz', 0.2)])
# 
# word_list = [leaf, reef, giraffe, cuff, eighteenth]
# wug_list = map(lambda x: Wug(x, change_set), ['waf'])


##### Learn the constraints, test the wugs, and print the results

evaluate.learn_constraints(word_list)
evaluate.test_wugs(wug_list)
# Only print if we're calling learner.py directly
if __name__ == '__main__':
    evaluate.write_output(word_list, wug_list)

# Some helpers for server.py
constraints = cons.faithfuls + cons.markeds
constraint_names = map(lambda x: x.func.__name__, constraints)