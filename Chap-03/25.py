#coding:utf-8
import json
import re

r = re.compile(u'\{基礎情報(.*?)\}')

f = open('jawiki-country.json', 'r')
lines = f.readlines()
f.close()

for line in lines:
    article_dict = json.loads(line)
    if article_dict["title"] == u"イギリス":
        England_text = article_dict["text"]

lines = England_text.replace("\n", "")

# print lines.encode('utf_8')

m = r.search(lines)

if m is not None:
    print m.group(1).encode('utf_8')
