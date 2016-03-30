import collections
import copy


def booleanify(value):
    """'False', 'false' and '0' will return False,
    everything else is considered True
    """
    return False if str(value).lower() in ('false', '0') else True


def make_hashable(obj):
    """from http://stackoverflow.com/questions/5884066/hashing-a-python-dictionary

    Makes a hashable object from a dictionary, list, tuple or set to any level, that contains
    only other hashable types (including any lists, tuples, sets, and
    dictionaries).

    Return hashable tuple
    """
    if isinstance(obj, collections.Hashable):
        return obj
    elif isinstance(obj, (tuple, set, list)):
        return tuple([make_hashable(element) for element in obj])

    new_obj = copy.deepcopy(obj)
    for k, v in new_obj.items():
        new_obj[k] = make_hashable(v)

    return tuple(sorted(new_obj.items()))
