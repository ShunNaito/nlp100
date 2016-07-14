#coding:utf-8
import json
import re

r = re.compile(u'File:(.*\.jpg)|ファイル:(.*\.jpg)')

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
        if m.group(1) is not None:
            print m.group(1).encode('utf_8')
        if m.group(2) is not None:
            print m.group(2).encode('utf_8')
