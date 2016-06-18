# coding: UTF-8

from operator import itemgetter
import sys

data_set = []  # データを格納するリスト

for line in open("hightemp.txt", 'r'):
    data = []
    data = line.split()
    data_set.append(data)

data_set.sort(key=itemgetter(2), reverse=True)

for line in data_set:
    for i in range(len(line)):
        if i != 0:
            sys.stdout.write("\t")
        sys.stdout.write(line[i])
    print
