#! /usr/bin/env python

import re

f = open("plurals.txt", 'r+')

def check_theta(line):
    word1, word2 = line.strip().split("\t")
    return not bool(re.search('T$', word1))
    
f.write("\n".join(filter(check_theta, f.read().replace("'", '').split("\n"))))