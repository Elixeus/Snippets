#!/usr/bin/env python
__author__ = 'Xia Wang'

'''
If in the dataset we have a column of categorical variables composed of string
values, and we want to convert the string values to numerical representations,
we can use the following way. (imagine we have categories saved in a column
called data['category'])
'''


ls = list(set(data['category']))
cat_dict = dict((j, i) for i, j in enumerate(ls))
data['category'] = map(lambda x: cat_dict[x], data['category'])
