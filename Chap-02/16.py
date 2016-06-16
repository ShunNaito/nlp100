# coding: UTF-8

num = input('行数を入力してください：')
f = open('hightemp.txt')
lines = f.readlines()
text = ""
i = 0

for i in range(len(lines)):
    if i % num == 0:
        if i != 0:
            output = "hightemp"+"_"+str(i/num)+".txt"
            fout = open(output, "w")
            fout.write(text)
            fout.close()
            text = ""
    text += lines[i]

output = "hightemp"+"_"+str(i/num+1)+".txt"
fout = open(output, "w")
fout.write(text)
fout.close()

f.close()
