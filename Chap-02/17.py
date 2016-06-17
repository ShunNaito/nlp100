# coding: UTF-8

data_col1 = []  # 1列目を格納するリスト

for line in open("hightemp.txt", 'r'):
    data = line.split()
    if data[0] not in data_col1:
        print data[0]
        data_col1.append(data[0])  # 1列目を表示
