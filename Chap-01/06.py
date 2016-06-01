#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bigram(input):
    ret = []
    for (a, b) in zip(input, input[1:]):
        ret.append(a + b)
    return ret

str1 = 'paraparaparadise'
str2 = 'paragraph'

x = bigram(str1)
y = bigram(str2)

z = set(x)
z |= set(y)
print z

z = set(x)
z -= set(y)
print z

z = set(x)
z &= set(y)
print z

print "se" in x
print "se" in y
