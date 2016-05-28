# coding:utf-8
str1 = u"パトカー"
str2 = u"タクシー"
str = ""

for i in range(len(str1)):
    str += str1[i] + str2[i]

print str.encode('utf_8')
