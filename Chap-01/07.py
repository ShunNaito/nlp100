#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sentenceGenerator(x, y, z):
    text = str(x) + "時の" + y + "は" + str(z)
    return text


print sentenceGenerator(12, "気温", 22.4)
