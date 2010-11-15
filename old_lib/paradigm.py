# Initializes a paradigm from a line in a .pairs file, to be specified later
# Each paradigm contains two words, which are a lists of syllables
# Presumably in the future it will also do serialization and database transactions...

import sys

class Paradigm:
  
  def __init__(self, form1, form2):
    self.forms = map(self.convert_form, (form1, form2))
      
  def convert_form(self, form):
    return map(lambda s: Syllable(s), form.split('.'))
  
  def form1():
    return forms[0]
  
  def form2():
    return forms[1]
      

# Contains a list of segments, and stress
class Syllable:
  def __init__(self, syll):
    self.segments = syll
    self.stress = "heavy"
  
# Reads in attributes from a .features file, to be specified eventually
class Segment:
  pass
