import re

def hash_object(my_object):
    import re
    my_hash = {}
    for method in dir(my_object):
        if not re.match('__.*__', method):
            my_hash[method] = my_object.__dict__[method]
    return my_hash
    

def open_sep(file_path, sep):
    return map(lambda x: x.split(sep), open(file_path).readlines())
    
def open_csv(file_path):
    return open_sep(file_path, ',')

    
def strip_quotes(string):
    return re.match('"(.*)"', string).group(1)