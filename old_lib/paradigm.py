# Initializes a paradigm from a line in a .pairs file, to be specified later
# Each paradigm contains two words, which are a lists of syllables
# Presumably in the future it will also do serialization and database transactions...

import sys

def make_pair(pair):
  word, prob = pair
  return (Form(word), prob)

class Paradigm:
  
  def __init__(self, base, *derivatives):
    self.base = Form(base)
    self.derivatives = map(make_pair, derivatives)
      
  def convert_form(self, form):
    return map(lambda s: Syllable(s), form.split('.'))

class Form:
  def __init__(self, form):
    # Syllabify function!
    # Get syllables somehow...
    self.syllables = map(lambda s, x: Syllable(s, x), [(syll1, stress1), (syll2, stress2), (syll3, stress3)])

# Contains a list of segments, and stress
class Syllable:
  def __init__(self, segments, stress):
    self.segments = segments
    self.stress = stress
  
# Reads in attributes from a .features file, to be specified eventually
class Segment:
  pass
