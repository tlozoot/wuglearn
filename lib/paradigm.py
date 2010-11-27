# coding=utf8

import re
import alignment
from segment import Segment
from form import Form

class Paradigm:
    '''A paradigm consists of a base form and a list of derivatives (accepted as pairs)'''
    '''Also some metadata, such as orthography and frequency'''
    def __init__(self, base, derivatives, ortho=None, freq=None):
        self.base = Form(base)
        self.ortho = ortho
        self.freq = freq
        self.derivatives = map(lambda d: Derivative(*d), derivatives)
        
    def best_derivative(self):
        return max(self.derivatives, key = lambda x: x.prob).form
    
    def symbol(self, derivative):
        return u' ☞ ' if derivative.form == self.best_derivative() else '     '

class Derivative:
    '''A derivative has a Form and a probability'''
    def __init__(self, form, prob):
        self.probability = self.prob = prob
        self.form = Form(form)


# A syllable is a list of segments, with stress
class Syllable:
    def __init__(self, segments, stress):
        self.segments = segments
        self.stress = stress
        # At some point, we want to split up syllables into segments in some smart way