# coding: UTF-8

from collections import Counter
import MeCab
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

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

word_list = []

for sentence in morpheme_set:
    for morpheme in sentence:
        word_list.append(morpheme["surface"])

counts = Counter(word_list)

X = range(1, 11)
Y = []
word_list_10 = []

for word, cnt in counts.most_common(10):
    word_list_10.append(word.decode('utf-8'))
    Y.append(cnt)

fp = FontProperties(fname='/Users/naitoushun/Library/Fonts/ipag.ttf')
plt.bar(X, Y, align="center")
plt.xticks(X, word_list_10, fontproperties=fp)
plt.show()