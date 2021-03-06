# coding=utf8

import re

from form import Form

class Wug:
    def __init__(self, ipa, change_set, ortho=None, human_voiciness=0, mingen_voiciness=0):
        self.base = Form(ipa)
        self.ortho = ortho
        self.human_voiciness = human_voiciness
        self.mingen_voiciness = mingen_voiciness
        self.derivatives = map(lambda change: change(self.base), change_set)
        self.scores = {}
        for derivative in self.derivatives:
            self.scores[derivative.to_u()] = {}
    
    def avg_score(self, derivative):
        return sum(self.scores[derivative.to_u()].values()) # / len(self.derivatives)
        
    def prob(self, derivative):
        denominator = sum(map(lambda x: self.avg_score(x), self.derivatives))
        return 1 - self.avg_score(derivative) / denominator
    
    def voiciness(self):
        voiced_form = ''
        for derivative in self.derivatives:
            if re.search('z$', derivative.to_u()):
                voiced_form = derivative
        return (6 * self.prob(voiced_form)) + 1
        
    def best_derivative(self):
        best_deriv = u''
        best_score = 10000
        for derivative in self.derivatives:
            score = self.avg_score(derivative) 
            if score < best_score:
                best_deriv = derivative
                best_score = score
        return best_deriv
        
    def symbol(self, derivative):
        return u' ☞ ' if derivative == self.best_derivative() else '     '
    