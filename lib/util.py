# We should split this into a module?
def hash_object(my_object):
  import re
  my_hash = {}
  for method in dir(my_object):
    if not re.match('__.*__', method):
      my_hash[method] = my_object.__dict__[method]
  return my_hash