#!/usr/bin/env python
import bisect


def grade(score, breakpoints=[60, 70, 80, 90],
          grades='FDCBA'):
    '''
    Convert points to grades. Each grade is separated by 10 points'''
    i = bisect.bisect_right(breakpoints, score)
    return grades[i]


if __name__ == '__main__':
    finals = [grade(score) for score in [33, 99, 77]]
    print finals
