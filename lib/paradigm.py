# Initializes a paradigm from a line in a .pairs file, to be specified later
# Each paradigm contains two words, which are a lists of syllables
# This class also contains methods for comparing paradigms
# Presumably in the future it will also do serialization and database transactions...
class Paradigm:  
  def __init__(self, line):
    word1, word2 = line.strip().split("\t")
    print word1
    
  def needleman(self):
    pass
    
  def levenshtein(self):
    pass


# Contains a list of features, and stress
class Syllable:
  pass
  
# Reads in attributes from a .features file, to be specified eventually
class Feature:
  pass
