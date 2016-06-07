# coding: UTF-8

f = open('hightemp.txt')
lines = f.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
for line in lines:
    print line.expandtabs(1),
f.close()
# lines: リスト。要素は1行の文字列データ
