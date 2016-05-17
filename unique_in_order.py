#!/usr/bin/python


def unique_in_order(iterable):
    '''
    choose only the non-consecutive chars in a string
    and make them a list.
    '''

    ls = [i for i in iterable]
    if len(ls) <= 1:
        return ls
    else:
        return [ls[index] for index in range(len(ls) - 1)
                if ls[index] != ls[index + 1]] + [ls[-1]]


def unique_in_order(iterable):
    '''
    Sometimes a simple for loop is better than a list comprehension.
    '''

    result = []
    prev = None
    for char in iterable:
        if char != prev:
            result.append(char)
            prev = char
    return result


def unique_in_order(iterable):
    '''
    Itertools built-in
    '''

    from itertools import groupby
    return [k for (k, _) in groupby(iterable)]


def unique_in_order(iterable):
    '''
    more elegant solution than my own
    '''
    ls = [i for i in iterable]
    return [val for index, val in enumerate(ls)
            if i == 0 or ls[index - 1] != val]
