# coding: UTF-8

f = open('hightemp.txt')
lines = f.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines: リスト。要素は1行の文字列データ

print len(lines)
