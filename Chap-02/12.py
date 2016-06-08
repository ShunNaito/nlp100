# coding: UTF-8

fin = open('hightemp.txt')
lines = fin.readlines()  # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
fout_col1 = open("col1.txt", "w")  # col1.txtファイルを書き込みモードで作成
fout_col2 = open("col2.txt", "w")  # col2.txtファイルを書き込みモードで作成
for line in lines:
    data = line.split()
    fout_col1.writelines(str(data[0]) + "\n")  # 1列目を書き込み
    fout_col2.writelines(str(data[1]) + "\n")  # 2列目を書き込み
fin.close()
# lines: リスト。要素は1行の文字列データ
