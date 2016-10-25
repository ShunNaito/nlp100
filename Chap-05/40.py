#!/usr/bin/env python
# coding: utf-8

class Morph:
  def __init__(self, surface, base, pos, pos1):
    self.surface = surface
    self.base = base
    self.pos = pos
    self.pos1 = pos1

fin = open('neko.txt.cabocha')
lines = fin.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
fin.close()

sentence = []
morpheme_set = []

for line in lines:
    morpheme_list = line.split('\t')
    surface = morpheme_list[0]
    if surface.startswith("*"):
      continue
    if surface == "EOS\n":
        morpheme_set.append(sentence)
        sentence = []
    else:
        feature = morpheme_list[1].split(',')
        morph = Morph(surface, feature[6], feature[0], feature[1])
        sentence.append(morph)


for morpheme in morpheme_set[2]:
  print morpheme.surface + "\t" + morpheme.base + ", " + morpheme.pos + ", " + morpheme.pos1