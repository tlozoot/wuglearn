#! /usr/bin/env python

class Paradigm:
  
  def __init__(self, line):
    word1, word2 = line.strip().split("\t")
    print word1
    
  def needleman(self):
    pass
    
  def levenshtein(self):
    pass
    

paradigms = map(lambda l: Paradigm(l), open("pairs.txt").readlines())