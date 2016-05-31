#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bigram(input):
    for (a, b) in zip(input, input[1:]):
        print a, b

text = 'I am an NLPer'
list = text.split(" ")  # リスト
text = text.replace(" ", "")  # 文字列

bigram(list)  # 単語bi-gram
bigram(text)  # 文字bi-gram
