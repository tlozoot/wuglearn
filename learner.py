#! /usr/bin/python
# coding=utf8

# See what you're importing in lib/__init__.py
from lib import *

# Align two Forms
knife = paradigm.Form('naif')
knives = paradigm.Form('naivz')
print "alignment of knife and knives:", alignment.align_forms(knife, knives)

# Get info about segments

# Read in a file from somewhere in data-
# This part will change; we want to be pretty agnostic about how these things are formatted, at least for now