#!/usr/bin/env python
import operator
from string import punctuation

# first way
counts = {}
with open('file.txt', 'r') as fh:
    for line in fh:
        words = line.lower().translate(None, punctuation).split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
# sort the dict by value
sorted_counts = sorted(counts.items(),
                       key=operator.itemgetter[1],
                       reverse=True)
# sorted_counts is a list of key-value tuples sorted from high to low
print sorted_counts


# second way
counts = {}
with open('file.txt', 'r') as fh:
    text = fh.read()
word_ls = text.lower().translate(None, punctuation).split()
for word in word_ls:
    counts[word] = word_ls.count(word)
sorted_counts = sorted(counts.items(),
                       key=operator.itemgetter[1],
                       reverse=True)
print sorted_counts
