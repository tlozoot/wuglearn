#! /usr/bin/env python

from lib.paradigms.paradigm import *  

paradigms = map(lambda l: Paradigm(l), open("lib/needle_test.pairs").readlines())
