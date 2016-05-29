# coding:utf-8
str = ("Now I need a drink, alcoholic of course, "
       "after the heavy lectures involving quantum mechanics.")

list = str.replace(",", "").replace(".", "").split(" ")

for i in range(len(list)):
    list[i] = len(list[i])

print list
