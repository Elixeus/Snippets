#!/usr/bin/python
'''
choose only the non-consecutive chars in a string
and make them a list.
'''


def unique_in_order(iterable):
    ls = [i for i in iterable]
    if len(ls) <= 1:
        return ls
    else:
        return [ls[index] for index in range(len(ls) - 1)
                if ls[index] != ls[index + 1]] + [ls[-1]]
'''
Sometimes a simple for loop is better than a list comprehension.
'''


def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable:
        if char != prev:
            result.append(char)
            prev = char
    return result
