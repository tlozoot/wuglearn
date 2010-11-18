# Vector.py
# It would probably be better to use a library for this stuff...

def dot_prod(vec1, vec2):
  '''Just the dot product of two vectors'''
  return sum(map(lambda x: x[0] * x[1], zip(vec1, vec2)))

def magnitude(vec):
  '''The magnitude of a vector'''
  return sum(map(lambda x: x **2, vec)) ** 0.5

def cosine_sim(vec1, vec2):
  ''' '''
  if magnitude(vec1) != 0 and magnitude(vec2) != 0:
    return dot_prod(vec1, vec2) / (magnitude(vec1) * magnitude(vec2))
