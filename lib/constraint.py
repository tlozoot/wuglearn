##### CONSTRAINTS.PY #####

# Contains a class definition for Constraint
# Plus, a bunch of actual constraint functions

import alignment

class Constraint:
  def __init__(self, func):
    self.func = func
    self.scores = []
  
  def avg_score(self):
    return sum(scores) / len(scores)

  
# FAITHFULNESS CONSTRAINTS

def id_voice_s1(form1, form2):
  root_s1, deriv_s1 = map(lambda x: x.syllables()[0], [form1, form2])
  a = alignment.align(root_s1, deriv_s1)[0]
  score = 0
  for pair in a:
    if (pair[0].feature('voice') != pair[1].feature('voice')) and pair[0].ipa != '' and pair[1].ipa != '':
      score += 1
  return score

def id_voice_stressed(form1, form2):
  return 0
  
def id_voice_root(form1, form2):
  return 0

def id_voice_affix(form1, form2):
  return 0
  
faithfuls = [id_voice_s1, id_voice_stressed, id_voice_root, id_voice_affix]
  
# MARKEDNESS CONSTRAINTS

def agree_voice(form):
  segs = form.segments()
  score = 0
  for i in range(len(segs) - 1):
    if segs[i].feature('voice') != segs[i + 1].feature('voice'):
      score += 1
  return score

def no_long_vowels(form):
  return 0

def no_long_vowels_before_f(form):
  return 0

markeds = [agree_voice, no_long_vowels, no_long_vowels_before_f]