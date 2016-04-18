#!/bin/bash
# this is a naive bash script to count words of a text file
if [ $# -eq 0 ]
then
    echo 'No argument passed. Command format: wordcount.sh foo.txt'
else
    tr 'A-Z' 'a-z' < $1 | tr -sc 'A-Za-z' '\n' | sort | uniq -c | sort -n -r | less
fi
