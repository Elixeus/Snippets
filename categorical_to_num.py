#!/usr/bin/env python
__author__ = 'Xia Wang'

'''
If in the dataset we have a column of categorical variables composed of string
values, and we want to convert the string values to numerical representations,
we can use the following way. (imagine we have categories saved in a column
called data['category'])
'''


# ls = list(set(data['category']))
# #cat_dict = dict((j, i) for i, j in enumerate(ls))
# cat_dict = {j: i for i, j in enumerate(ls)}
# data['category'] = map(lambda x: cat_dict[x], data['category'])


def categorical_to_num(categos):
    '''
    convert the categorical variables to dummy numbers.
    return a list that contains a dummy number corresponding to each
    categorical value.

    parameters:
    ------------
    categos: the iterable that contains all the categorical values'''
    cat_dict = {cate: num for num, cate in
                enumerate(sorted(list(set(categos))))}
    return tuple(map(lambda x: cat_dict[x], categos))


if __name__ == '__main__':
    ls = list('ACBDE')
    print categorical_to_num(ls)
