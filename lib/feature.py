# coding=utf8

#### FEATURE.PY ######
# Lets you do things like this:

# print "get_value:", feature.get_value(u'ŋ', 'voice')
# print "get_hash:", feature.get_hash(u'ŋ')
# print "get_array:", feature.get_array(u'ŋ')

# Avoid calling FEATURES[segment][feature] directly--this implementation change!

import re

# A function to strip quotes and whitespace
def clean_record(rec):
  return re.sub('"', '', rec).strip()

# Get the file into a row of columns
feature_rows = map(lambda row: row.split(','), open(__package__ + '/features.csv').readlines())
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


#### PUBLIC FUNCTIONS ####

def get_value(segment, feature):
  return FEATURES[segment][feature]
  
def get_hash(segment):
  return FEATURES[segment]

# A feature array, sorted alphabetically by name of the feature
def get_array(segment):
  return map(lambda x: x[1], sorted(FEATURES[segment].items()))