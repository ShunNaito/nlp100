#coding:utf-8
import json
import re

r = re.compile(u'\|(.*)\s=\s(.*)|(\*+\{\{lang.*)')

f = open('jawiki-country.json', 'r')
lines = f.readlines()
f.close()

for line in lines:
    article_dict = json.loads(line)
    if article_dict["title"] == u"イギリス":
        England_text = article_dict["text"]

lines = England_text.split("\n")

basicInformationDict = {}

for line in lines:
    m = r.search(line)
    if m is not None:
        if m.group(3) is not None:
            tmp = (basicInformationDict.keys()
                   [len(basicInformationDict.keys()) - 1])
            basicInformationDict[tmp] += m.group(3)
        else:
            basicInformationDict[m.group(1)] = m.group(2)

# 辞書のitems()メソッドで全てのキー(key), 値(value)をたどる
for k, v in basicInformationDict.items():   # for/if文では文末のコロン「:」を忘れないように
    print k.encode('utf_8'), v.encode('utf_8')
