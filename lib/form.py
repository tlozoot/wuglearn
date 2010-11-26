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
    
  def to_u(self):
    return ''.join(map(lambda x: x.ipa, self.segments()))
  
  def sonority(self):
    return map(lambda x: x.sonority(), self.segments())
  	
  def syllables(self):
  	sylls = []
  	sylls.append([self.segments()[0]])

  	for x in range(1,len(self.segments())-1):
  	  if self.segments()[x-1].sonority() <  self.segments()[x].sonority():
  	    sylls[len(sylls)-1].append(self.segments()[x])
  	  else:
  	    if self.segments()[x].sonority() >=  self.segments()[x+1].sonority(): 
  	      sylls[len(sylls)-1].append(self.segments()[x])
  	    else:
  	      sylls.append([self.segments()[x]])
  	      
  	sylls[len(sylls)-1].append(self.segments()[len(self.segments())-1])
  	return sylls