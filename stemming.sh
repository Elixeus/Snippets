#!/bin/bash
# This is a naive implementation of the Porter's stemming algorithm in unix
if [ $# -eq 0 ]
then
    echo 'No argument passed. Command format: stemming.sh foo.txt'
else
    tr -sc 'A-Za-z' '\n' < Shake.txt | tr 'A-Z' 'a-z' | grep '[aeiou].*ing$' | sort | uniq -c | sort -n -r | less
fi
