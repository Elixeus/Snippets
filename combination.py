#!/usr/bin/env python
from itertools import combinations


def combo(iterable, num_elements=2):
    '''
    combo is a function to make combiB
    '''
    return [i for i in combinations(iterable, num_elements)]


if __name__ == '__main__':
    x = combo(iterable=range(10), num_elements=3)
    print x
