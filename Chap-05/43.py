#!/usr/bin/env python
# coding: utf-8
import re


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

fin = open('neko.txt.cabocha')
lines = fin.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
fin.close()

sentence = []
chunk_set = []
clause_morphs = []
dst = ""
srcs = ""

for line in lines:
    morpheme_list = line.split('\t')
    surface = morpheme_list[0]
    if surface == "EOS\n" or surface.startswith("*"):
        if(clause_morphs):
            chunk = Chunk(clause_morphs, dst, srcs)
            sentence.append(chunk)
        clause_morphs = []
        if surface == "EOS\n":
            chunk_set.append(sentence)
            sentence = []
        if surface.startswith("*"):
            dependency = surface.split(' ')
            dst = dependency[2]
            srcs = dependency[1]
    else:
        feature = morpheme_list[1].split(',')
        morph = Morph(surface, feature[6], feature[0], feature[1])
        clause_morphs.append(morph)

for sentence in chunk_set:
    for i in range(len(sentence) - 1):  # 最後の文節は除外
        modifiedSource = ""  # 係り元
        noun = False
        for morph in sentence[i].morphs:
            # 記号は除外する
            if(morph.pos == "記号"):
                continue
            modifiedSource += morph.surface
            if(morph.pos == "名詞"):
                noun = True
        if(noun is False):
            continue
        destinationNumber = int(sentence[i].dst.replace("D", ""))
        modifyingDestination = ""  # 係り先
        verb = False
        for morph in sentence[destinationNumber].morphs:
            # 記号は除外する
            if(morph.pos == "記号"):
                continue
            if(morph.pos == "動詞"):
                verb = True
            modifyingDestination += morph.surface
        if(verb is False):
            continue
        print modifiedSource + "\t" + modifyingDestination
