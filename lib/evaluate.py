# coding=utf8

import constraint as cons
import alignment

def learn_constraints(word_list):
  '''Learn the faithfulness and markedness constraints based on a word list'''
  for con in cons.faithfuls:
    for paradigm in word_list:
      for derivative in paradigm.derivatives:
        for a in alignment.align_forms(paradigm.base, derivative.form):
          score = con.func(paradigm.base, derivative.form, a)
          con.scores[derivative.form.ipa_string()] = (score * derivative.probability)
          
  for con in cons.markeds:
    for paradigm in word_list:
      for derivative in paradigm.derivatives:
        score = con.func(derivative.form)
        con.scores[derivative.form.ipa_string()] = (score * derivative.probability)
        

def test_wugs(wug_list, change_set):
  '''Get some wug plurals out of the constraints'''
  for wug in wug_list:
    for change in change_set:
      wug_deriv = change(wug.base)
      wug.con_scores[wug_deriv.ipa_string()] = {}
      for a in alignment.align_forms(wug.base, wug_deriv):
        for con in cons.faithfuls + cons.markeds:
          if con.type == 'faithfulness':
            score = con.func(wug.base, wug_deriv, a)
          elif con.type == 'markedness':
            score = con.func(wug_deriv)        
          con.wug_scores[wug_deriv.ipa_string()] = wug.con_scores[wug_deriv.ipa_string()][con.func.__name__] = score * con.avg_score()
      
      

def print_table(word_list, wug_list, change_set, faithfuls, markeds):
  '''Debugging code to print the table out'''
  constraints = faithfuls + markeds
  print "Paradigm\t    derivative\tp\t" ,
  print "\t".join(map(lambda x: x.func.__name__, constraints)), "\tAverage"
  for paradigm in word_list:
    print paradigm.base.ipa_string()
    for derivative in paradigm.derivatives:
      symbol = ' ☞ ' if derivative.form == paradigm.best_derivative() else '   '
      print "\t\t", symbol, derivative.form.ipa_string(), "\t", derivative.prob, "\t" ,
      for cons in constraints:
        print cons.scores[derivative.form.ipa_string()], "\t\t", 
      print
  print "\nAVERAGES\t\t\t\t",
  for cons in constraints:
    print cons.avg_score(), "\t\t",
  print "\n\nWUGS\n"
  for wug in wug_list:
    print wug.base.ipa_string(),
    for change in change_set:
      wug_deriv = change(wug.base)
      symbol = ' ☞ ' if wug_deriv.ipa_string() == wug.best_derivative() else '   '
      print "\t\t", symbol, wug_deriv.ipa_string(), "\t", round(wug.prob(wug_deriv), 4), "\t",
      for cons in constraints:
        print round(cons.wug_scores[wug_deriv.ipa_string()], 4), "\t\t",
      print wug.avg_score(wug_deriv.ipa_string())
  
  
