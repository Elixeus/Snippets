#!/usr/bin/env python
import operator


counts = {}
with open('file.txt', 'r') as fh:
    for line in fh:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
# sort the dict by value
sorted_counts = sorted(counts.items(),
                       key=operator.itemgetter[1],
                       reverse=True)
# sorted_counts is a list of key-value tuples sorted from high to low
print sorted_counts
