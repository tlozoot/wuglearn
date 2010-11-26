##### CONSTRAINTS.PY #####
# coding=utf-8

# Contains a class definition for Constraint
# Plus, a bunch of actual constraint functions

import alignment

class Constraint:
  def __init__(self, func, constraint_type):
    self.func = func
    self.scores = {}
    self.type = constraint_type
  
  def avg_score(self):
    return sum(self.scores.values()) / len(self.scores)

  
# FAITHFULNESS CONSTRAINTS

def id_voice_s1(form1, form2, alignment):
  score = 0
  syl_1_counter = 0
  for pair in alignment:
    if pair[0].ipa != '':    
      if syl_1_counter < len(form1.syllables()[0]):
        syl_1_counter += 1
        if pair[0].feature('voice') != pair[1].feature('voice'):
          score += 1
  return score

def id_voice_stressed(form1, form2, alignment):
  return 0
  
def id_voice_root(form1, form2, alignment):
  score = 0
  for pair in alignment:
    if pair[0].ipa != '':
      if pair[0].feature('voice') != pair[1].feature('voice'):
        score += 1
  return score

def id_voice_affix(form1, form2, alignment):
  # Important-- this should NOT be specific to assuming a 'z' affix!
  # It seems like we'll have to consider passing the affix into these constraint functions...
  if form2.segments()[-1].feature('voice') == -1:
    return 1
  else: return 0
  
  
# MARKEDNESS CONSTRAINTS

def agree_voice(form):
  segs = form.segments()
  score = 0
  for i in range(len(segs) - 1):
    if segs[i].feature('voice') != segs[i + 1].feature('voice'):
      score += 1
  return score

def no_long_v(form):
  segs = form.segments()
  score = 0
  for seg in segs:
    if seg.feature('consonantal') == -1 and seg.ipa != 'w':
      if seg.feature('tense') == 1 or seg.feature('low') == 1:
        score += 1
  return score

def no_long_v_f(form):
  segs = form.segments()
  score = 0
  seen_V = 0
  for i in range(len(segs)):
    if segs[i].feature('consonantal')==-1 and (segs[i].feature('tense')==1 or segs[i].feature('low')==1):
      seen_V = 1
    if seen_V==1 and segs[i].feature('continuant')==1 and segs[i].feature('sonorant')==-1 and segs[i].feature('voice')==-1:
      score += 1
    if segs[i].feature('sonorant')==-1:
      seen_V = 0
  return score


# CONSTRAINT LISTS
faithfuls = map(lambda x: Constraint(x, 'faithfulness'), [id_voice_s1, id_voice_root, id_voice_affix])
markeds = map(lambda x: Constraint(x, 'markedness'), [no_long_v_f, no_long_v])