# coding=utf8

import re
import alignment
from segment import Segment
from form import Form

class Paradigm:
    '''A paradigm consists of a base form and a list of derivatives (accepted as pairs)'''
    '''Also some metadata, such as orthography and frequency'''
    def __init__(self, base, derivatives, ortho=None, freq=None):
        if base.__class__ == Form:
            self.base = base
        else:
            self.base = Form(base)
        self.ortho = ortho
        self.freq = freq
        self.derivatives = map(lambda d: Derivative(*d), derivatives)
        
    def best_derivative(self):
        return max(self.derivatives, key = lambda x: x.prob).form
    
    def voiciness(self):
        best_deriv = self.best_derivative()
        best_deriv_prob = max(self.derivatives, key = lambda x: x.prob).prob
        if best_deriv.segments()[-1].feature('voice') == 1:
            return best_deriv_prob * 6 + 1
        else:
            return (1 - best_deriv_prob) * 6 + 1
            
    
    def symbol(self, derivative):
        return u' ☞ ' if derivative.form == self.best_derivative() else '     '

class Derivative:
    '''A derivative has a Form and a probability'''
    def __init__(self, form, prob):
        self.probability = self.prob = prob
        if form.__class__ == Form:
            self.form = form
        else:
            self.form = Form(form)


# A syllable is a list of segments, with stress
class Syllable:
    def __init__(self, segments, stress):
        self.segments = segments
        self.stress = stress
        # At some point, we want to split up syllables into segments in some smart way