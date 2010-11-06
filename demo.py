#! /usr/bin/env python

import lib.needleman

def process_lines(line):
  word1, word2 = line.strip().split("\t")
  lib.needleman.nw_test(word1, word2)

paradigms = map(lambda l: process_lines(l), open("lib/needle_test.pairs").readlines())