# coding=utf8

import re
import alignment

class Paradigm:
  '''A paradigm consists of a base form and a list of derivatives (accepted as pairs)'''
  def __init__(self, base, derivatives):
    self.base = Form(base)
    self.derivatives = map(lambda d: Derivative(d[0], d[1]), derivatives)
    
  def best_derivative(self):
    return max(self.derivatives, key = lambda x: x.prob)

class Derivative:
  '''A derivative has a Form and a probability'''
  def __init__(self, form, prob):
    self.probability = prob
    self.prob = prob
    self.form = Form(form)

# A form is just a list of syllables
class Form:
  def __init__(self, form):
    self.word = form # to be replaced by stuff below this!
    # We need a syllabify function...
    # self.syllables = map(lambda s, x: Syllable(s, x), [(syll1, stress1), (syll2, stress2), (syll3, stress3)])
  
  def segments(self):
    return list(self.word)

# A syllable is a list of segments, with stress
class Syllable:
  def __init__(self, segments, stress):
    self.segments = segments
    self.stress = stress
    # At some point, we want to split up syllables into segments in some smart way