# coding=utf8

import re

# A helper function for Paradigm
def make_pair(pair):
  word, prob = pair
  return (Form(word), prob)

# A paradigm consists of a base form, and then pairs of derivatives (Form, probability)
class Paradigm:
  def __init__(self, base, *derivatives):
    self.base = Form(base)
    self.derivatives = map(make_pair, derivatives)

# A form is just a list of syllables
class Form:
  def __init__(self, form):
    # Syllabify function!
    # Get syllables somehow...
    self.syllables = map(lambda s, x: Syllable(s, x), [(syll1, stress1), (syll2, stress2), (syll3, stress3)])

# A syllable is a list of segments, with stress
class Syllable:
  def __init__(self, segments, stress):
    self.segments = segments
    self.stress = stress
    # At some point, we want to split up syllables into segments in some smart way
    
    
#### FEATURES!!!

# A function to strip quotes and whitespace
def clean_record(rec):
  return re.sub('"', '', rec).strip()

# Get the file into a row of columns
feature_rows = map(lambda row: row.split(','), open('features.csv').readlines())
for row in feature_rows: row.pop(0) # get rid of unwanted rows

# Get the names of the features into an array
feature_names = map(lambda x: clean_record(x), feature_rows.pop(0))

# Initialize the hash of every feature
FEATURES = {}
for row in feature_rows:
  ipa = row.pop(0)     # Your symbol should be the first element of the row
  item_features = {}   # Create a hash for each feature
  for i in range(len(row)): item_features[feature_names[i+1]] = int(row[i])
  FEATURES[unicode(clean_record(ipa), 'utf8')] = item_features
  
  