#coding:utf-8
import json
import re


def remove_internal_link(m):
    m2 = r2.search(m.group().encode('utf_8'))
    if m2.group(3) is not None:
        extracted_string = m2.group(3)
    else:
        extracted_string = m2.group(1)
    return extracted_string.decode('utf_8')

r = re.compile(u'\|(.*)\s=\s(.*)|(\*+\{\{lang.*)')
r2 = re.compile(u'\[\[(.*?)(\|(.+?))*]\]')

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
            officialCountry = (basicInformationDict.keys()
                               [len(basicInformationDict.keys()) - 1])
            basicInformationDict[officialCountry] += m.group(3)
        else:
            text = m.group(2).replace("'", "")
            str_internal_link_removed = re.sub(
                u'(\[\[(.+?)\]\])+', remove_internal_link, text)
            str_HTML_tags_removed = re.sub(
                u'(\<(.+?)\>)+', "", str_internal_link_removed)
            str_external_link_removed = re.sub(
                u'(\[(.+?)\])+', "", str_HTML_tags_removed)
            basicInformationDict[m.group(1)] = str_external_link_removed

# 辞書のitems()メソッドで全てのキー(key), 値(value)をたどる
# for/if文では文末のコロン「:」を忘れないように
for k, v in sorted(basicInformationDict.items(), key=lambda x: x[0]):
    print k.encode('utf_8'), v.encode('utf_8')
