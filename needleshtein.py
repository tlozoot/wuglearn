#! /usr/bin/env python

from lib.paradigm import *

paradigms = map(lambda l: Paradigm(l), open("lib/needle_test.pairs").readlines())
