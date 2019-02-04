#!/usr/bin/env python

# import necessary packages
from sys import argv, exit
from itertools import permutations
import enchant as en

# clear out "script name" argument
argv.pop(0)


# get letters - if no letters, tell user
try:
    letters = argv.pop(0)
except IndexError:
    print("You need to pass the letters as an argument!")
    exit(1)


# get target length
if len(argv) > 0:
    num = int(argv.pop(0))
else:
    num = len(letters)


# set up dictionary for pyenchant
d = en.Dict("en_US")


# get possible letter combinations
letters = list(letters)
perms = permutations(letters, num)


# check which are valid words, and store
words = []
for perm in perms:
    if d.check(''.join(perm)) and ''.join(perm) not in words:
        words.append(''.join(list(perm)))

# print the result
for word in words:
    print(word)
