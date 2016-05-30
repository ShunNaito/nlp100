# coding:utf-8
str = ("Hi He Lied Because Boron Could Not Oxidize Fluorine. "
       "New Nations Might Also Sign Peace Security Clause. Arthur King Can.")

list = str.replace(",", "").replace(".", "").split(" ")

numList = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dict = {}

for i in range(len(list)):
    if i+1 in numList:
        dict[list[i][:1:]] = i+1
    else:
        dict[list[i][:2:]] = i+1

for k, v in sorted(dict.items(), key=lambda x: x[1]):
    print k, v
