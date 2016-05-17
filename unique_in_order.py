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
