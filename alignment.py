#! /usr/bin/env python

import nwalign as nw
import lib

def score_alignment(word1, word2):
  print word1, word2
  return 1

# Parse input files
def make_pairs(paradigm):
  return map(lambda p: p.split("\n"), paradigm.split("\n~\n"))  
paradigms = map(make_pairs, open("lexicon.txt").read().split("\n\n%\n\n"))

# Score every pair
for paradigm in paradigms:
  max_score = 0
  best_pair = None
  for pair in paradigm:
    word1, word2 = pair
    score = lib.score_alignment(word1, word2)
    if score > max_score:
      max_score = score
      best_pair = pair
  print 'The best pair is: ' + str(pair) + ' with score ' + str(max_score) + "\n"
