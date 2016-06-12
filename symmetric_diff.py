#!/usr/env python
# coding=utf-8
from __future__ import print_function


'''
Find the difference between two sets
The different item can be either in set a or set b,
but not in both.
'''
a = set(range(10))
b = set(range(5, 15))
#  we can either use the symmetric_difference method
difference = a.symmetric_difference(b)
print(difference)
#  or we can use the ^ operator
print(a ^ b)
print(difference == a ^ b)
