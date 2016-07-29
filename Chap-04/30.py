# coding: UTF-8

import MeCab

fin = open('neko.txt')
lines = fin.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
fin.close()
# lines: リスト。要素は1行の文字列データ

tagger = MeCab.Tagger("-Ochasen")
sentence_set = []
sentence = {}

for line in lines:
    node = tagger.parseToNode(line)
    while node:
        sentence["surface"] = node.surface
        feature = node.feature.split(",")
        sentence["base"] = feature[6]
        sentence["pos"] = feature[0]
        sentence["pos1"] = feature[1]
        sentence_set.append(sentence.copy())
        node = node.next

for sentence in sentence_set:
    print sentence["surface"]
    print sentence["base"]
    print sentence["pos"]
    print sentence["pos1"]

fout = open("col1.txt", "w")
