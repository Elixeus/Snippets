#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NamedEntities:
    '''This class is created to help count and parse the KB items in the HC-KB excel file.
       It takes the column as an input.
       ------------------------------------
       countItem method calculates the total number of items in that
       column (ignore the empty lines automatically).
       getItems method return a list of usernames from that column.'''
    def __init__(self, strng):
        self._string = strng

    def count_items(self):
        return len([i for i in self._string.splitlines() if i])

    def get_items(self):
        return [i for i in self._string.splitlines() if i]

class Usernames(NamedEntities):
    def __init__(self, string):
        NamedEntities.__init__(self, string)
        
    def get_items(self):
        return [i[: i.find(' #')] if ' #' in i else i for i in self._string.splitlines()]
