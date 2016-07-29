# coding: UTF-8

import MeCab

fin = open('neko.txt.mecab')
lines = fin.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
fin.close()
# lines: リスト。要素は1行の文字列データ

tagger = MeCab.Tagger("-Ochasen")
sentence = []
morpheme_set = []
morpheme = {}

for line in lines:
    morpheme_list = line.split('\t')
    surface = morpheme_list[0]
    if surface == "EOS\n":
        morpheme_set.append(sentence)
        sentence = []
    else:
        morpheme["surface"] = surface
        feature = morpheme_list[1].split(',')
        morpheme["base"] = feature[6]
        morpheme["pos"] = feature[0]
        morpheme["pos1"] = feature[1]
        sentence.append(morpheme.copy())

for sentence in morpheme_set:
    for morpheme in sentence:
        print morpheme["surface"], morpheme["base"], morpheme["pos"], morpheme["pos1"]
    print 

# print morpheme_set
