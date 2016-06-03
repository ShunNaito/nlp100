#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cipher(str):
    char_list = list(str)
    text = ""
    for char in char_list:
        if char.islower():
            code_point = 219 - ord(char)
            text = text + unichr(code_point)
        else:
            text += char
    return text

str = cipher("Atbash is a simple substitution cipher for the Hebrew alphabet.")
print str
str = cipher(str)
print str
