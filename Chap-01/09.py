#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def Typoglycemia(text):
    text_list = text.split(" ")
    random_text = ""
    random_text_list = []
    for i in text_list:
        if(len(i) <= 4):
            random_text_list.append(i)
        else:
            random_word = i[:1:]
            random_str = list(i[1:-1:])
            random.shuffle(random_str)
            random_word += ''.join(random_str)
            random_word += i[-1::]
            random_text_list.append(random_word)
        random_text = " ".join(random_text_list)
    return random_text


random_text = Typoglycemia(("I couldn't believe that"
                            " I could actually understand "
                            "what I was reading : "
                            "the phenomenal power of the human mind ."))
print random_text
