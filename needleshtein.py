#! /usr/bin/env python

from lib.paradigm import *   

paradigms = map(lambda l: Paradigm(l), open("lib/pairs.txt").readlines())
