#coding:utf-8
import json

f = open('jawiki-country.json', 'r')
lines = f.readlines()
f.close()

for line in lines:
    article_dict = json.loads(line)
    if article_dict["title"] == u"イギリス":
        England_text = article_dict["text"]

lines = England_text.split("\n")
for line in lines:
    if u"Category" in line:
        print line.encode('utf_8')
