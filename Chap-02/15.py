# coding: UTF-8

num = input('行数を入力してください：')
f = open('hightemp.txt')
lines = f.readlines()

for line in lines[len(lines)-int(num)::]:
    print line.replace('\n', '')

f.close()
