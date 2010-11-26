from form import Form

class Wug:
  def __init__(self, ipa, change_set):
    self.base = Form(ipa)
    self.derivatives = map(lambda change: change(self.base), change_set)
    self.con_scores = {}
    # self.scores = {}
    # for derivative in self.derivatives:
      # self.scores[derivative.to_u()] = 
  
  def avg_score(self, derivative):
    return sum(self.con_scores[derivative].values()) / len(self.con_scores[derivative])
    
  def prob(self, derivative):
    denominator = sum(map(lambda x: self.avg_score(x), self.con_scores.keys()))
    return 1 - self.avg_score(derivative.ipa_string()) / denominator
  
  def voiciness(self, derivative):
    return (6 * self.prob(derivative)) + 1
    
  def best_derivative(self):
    best_deriv = u''
    best_score = 10000
    for deriv in self.con_scores.keys():
      score = self.avg_score(deriv) 
      if score < best_score:
        best_deriv = deriv
        best_score = score
    return best_deriv