#coding:utf-8
import json
import re

# r = re.compile('==+(\s)*(.+?)(\s)*==+')
r = re.compile('==(=+)*(\s)*(.+?)(\s)*(=+)*==')

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
        level = 1
        if m.group(1) is None:
            print m.group(3).encode('utf_8')
            print level
        else:
            for text in m.group(1):
                level = level + 1
            print m.group(3).encode('utf_8')
            print level
