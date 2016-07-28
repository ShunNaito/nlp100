# coding: UTF-8

import MeCab

f = open('neko.txt')
lines = f.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines: リスト。要素は1行の文字列データ

tagger = MeCab.Tagger("-Ochasen")

for line in lines:
    print tagger.parse(line)
