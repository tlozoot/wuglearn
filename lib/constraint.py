##### CONSTRAINTS.PY #####

# Contains a class definition for Constraint
# Plus, a bunch of actual constraint functions

class Constraint:
  def __init__(self, func):
    self.func = func
    
  
  
# FAITHFULNESS CONSTRAINTS

def id_voice_s1(form1, form2):
  return 0
  
def id_voice_root(form1, form2):
  return 0

def id_voice_affix(form1, form2):
  return 0
  
  
  
# MARKEDNESS CONSTRAINTS

def no_long_vowels(form):
  return 0

def no_long_vowels_before_f(form):
  return 0
  

