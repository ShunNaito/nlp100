# coding: UTF-8

data_col1 = []  # 1列目を格納するリスト
data_col2 = []  # 2列目を格納するリスト

fout = open("col1+2.txt", "w")

for line in open("col1.txt", 'r'):
    data_col1.append(line)

for line in open("col2.txt", 'r'):
    data_col2.append(line)

for i in range(len(data_col1)):
    fout.write(data_col1[i].replace('\n', '') + "\t" + data_col2[i])

fout.close()
