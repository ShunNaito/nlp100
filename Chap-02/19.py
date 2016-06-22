# coding: UTF-8

from collections import Counter
import sys

data_set = []  # データを格納するリスト
col1 = []      # 1列目のデータを格納するリスト

for line in open("hightemp.txt", 'r'):
    data = line.split()
    data_set.append(data)
    col1.append(data[0])

counter = Counter(col1)

word_dict = {}
for word, cnt in counter.most_common():
    for data in data_set:
        if data[0] == word:
            for i in range(len(data)):
                if i != 0:
                    sys.stdout.write("\t")
                sys.stdout.write(data[i])
            print
