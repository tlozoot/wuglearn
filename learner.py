#! /usr/bin/python
# coding=utf8

# See what this imports with help(lib)
from lib import *
from lib.segment import Segment
from lib.paradigm import Paradigm, Form

# Get info about a segment--now with OOP!
engma = Segment(u'ŋ'); n = Segment(u'n'); k = Segment(u'k')
print "Array of /n/:", n.array()
print "Hash of /k/:", k.hash()
print "Voiciness of /ŋ/:", engma.feature('voice')
print "Similarity of /ŋ/ and /n/:", engma.similarity(n)
print "Similarity of /ŋ/ and /k/--yikes!", engma.similarity(k), "\n"


# Take in a paradigm; align two forms
knife = Paradigm('naif', [('naivz', 0.9), ('naifs', 0.1)])
knife_sg = knife.base; knife_pl = knife.best_derivative()
print "The best plural of /naif/ is:", map(lambda x: x.ipa, knife_pl.segments())
print "Alignment of /naif/ and /naivz/:", alignment.align_forms_with_ipa(knife_sg, knife_pl)
print "Alignment scores for /naif/ and /naivz/:", alignment.align_forms_with_scores(knife_sg, knife_pl)

# Read in a file from somewhere in data-
# This part will change; we want to be pretty agnostic about how these things are formatted, at least for now