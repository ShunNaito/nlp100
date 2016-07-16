#coding:utf-8
import json
import re

r = re.compile(u'\|(.*)\s=\s(.*)')

f = open('jawiki-country.json', 'r')
lines = f.readlines()
f.close()

for line in lines:
    article_dict = json.loads(line)
    if article_dict["title"] == u"イギリス":
        England_text = article_dict["text"]

lines = England_text.split("\n")

for line in lines:
    m = r.search(line)
    if m is not None:
        print m.group(1).encode('utf_8'), m.group(2).encode('utf_8')
