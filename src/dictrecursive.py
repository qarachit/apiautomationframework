import collections

def dict_find_recursive(d, target, self):
    
    if not isinstance(d, collections.Mapping):
        return d == target
    else:
        for k in d:
            if dict_find_recursive(d[k], target) != False:
                    return k
        return False

def dict_flatten(d):
    if not isinstance(d, collections.Mapping):
        yield d
    else:
        for value in d:             
            for item in dict_flatten(d[value]):
                yield item