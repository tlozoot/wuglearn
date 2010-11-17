import re
from segment import Segment


# A form is just a list of syllables
class Form:
  def __init__(self, form):
    self.word = form # to be replaced by stuff below this!
    # We need a syllabify function...
    # self.syllables = map(lambda s, x: Syllable(s, x), [(syll1, stress1), (syll2, stress2), (syll3, stress3)])
  
  def segments(self):
    return map(lambda s: Segment(s), list(self.word))
    
  def ipa_string(self):
    return ''.join(map(lambda x: x.ipa, self.segments()))
  
