# coding=utf8

#### SEGMENT.PY ######
# Preferred usage is OO-style:
# engma = Segment(u'ŋ'); n = Segment(u'n'); k =  Segment(u'k')
# 
# print "Array of /n/:", n.array()
# print "Hash of /k/:", k.hash()
# print "Voiciness of /ŋ/:", engma.feature('voice')
# print "Similarity of /ŋ/ and /n/:", engma.similarity(n)
# print "Similarity of /ŋ/ and /k/--yikes!", engma.similarity(k)

# But you can still use get_feature, get_hash, get_array, etc
# Avoid calling FEATURES[segment][feature] directly--this implementation change!

import re
import vector

def clean_record(rec):
  '''Strips quotes and whitespace from a string'''
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

def get_feature(segment, feature):
  '''Returns the value of the given feature of the given segment'''
  return FEATURES[segment][feature]
  
def get_hash(segment):
  '''Returns a hash containing every feature of a given segment'''
  return FEATURES[segment]

def get_array(segment):
  '''Returns an array of every feature of a given segment, in some standard order'''
  return map(lambda x: x[1], sorted(FEATURES[segment].items()))
  
def similarity(seg1, seg2):
  '''The cosine similarity of two segments
      TODO: Weight importance of features! ŋ~n SHOULD NOT = ŋ~k '''
  return vector.cosine_sim(get_array(seg1), get_array(seg2))
  

class Segment:
  '''Some objects, if you like'''
  
  def __init__(self, ipa):
    self.ipa = ipa
  
  def hash(self):
    return get_hash(self.ipa)
  
  def array(self):
    return get_array(self.ipa)
  
  def feature(self, feature):
    return get_feature(self.ipa, feature)
    
  def similarity(self, segment):
    return similarity(self.ipa, segment.ipa)
  
  
  
