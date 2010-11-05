#! /usr/bin/env python

from lib.paradigm import Paradigm

paradigms = map(lambda l: Paradigm(l), open("lib/needle_test.pairs").readlines())
