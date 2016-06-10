# coding: UTF-8

num = input('行数を入力してください：')
f = open('hightemp.txt')
lines = f.readlines()

for i in range(int(num)):
    print lines[i].replace('\n', '')
f.close()
