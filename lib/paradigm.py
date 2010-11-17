# coding=utf8

import re
import alignment

# A paradigm consists of a base form, and then pairs of derivatives (Form, probability)
class Paradigm:
  def __init__(self, base, *derivatives):
    self.base = Form(base)
    
    def make_pair(pair):
      word, prob = pair
      return (Form(word), prob)
    self.derivatives = map(make_pair, derivatives)

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