#coding:utf-8
import json

f = open('jawiki-country.json', 'r')
lines = f.readlines()
f.close()
article_list = []

for line in lines:
    article_dict = json.loads(line)
    article_list.append(article_dict)

for line in article_list:
    if line["title"] == u"イギリス":
        print line["text"].encode('utf_8')
