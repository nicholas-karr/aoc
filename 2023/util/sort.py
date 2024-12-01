import functools

def sort(list, cmp):
    list.sort(key=functools.cmp_to_key(cmp))