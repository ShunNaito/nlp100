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


def remove_lang_link(m):
    m3 = r3.search(m.group().encode('utf_8'))
    if m3.group(3) is not None:
        extracted_string = m3.group(3)
    else:
        extracted_string = m3.group(1)
    return extracted_string.decode('utf_8')

r = re.compile(u'\|(.*)\s=\s(.*)|(\*+\{\{lang.*)')
r2 = re.compile(u'\[\[(.*?)(\|(.+?))*]\]')
r3 = re.compile(u'\{\{(.*?)(\|(.+?))*}\}')

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
            str_lang_link_removed = re.sub(
                u'(\{\{(.+?)\}\})+', remove_lang_link,
                m.group(3))
            # print str_lang_link_removed.encode('utf_8')
            str_HTML_tags_removed = re.sub(
                u'(\<(.+?)\>)+', "", str_lang_link_removed)
            str_lang_name_extracted = re.sub(
                u'（\[\[(.+?)\]\]）', u"（" + r"\1" + u"）", str_HTML_tags_removed)
            basicInformationDict[officialCountry] += str_lang_name_extracted
        else:
            text = m.group(2).replace("'", "")
            str_internal_link_removed = re.sub(
                u'(\[\[(.+?)\]\])+', remove_internal_link, text)
            str_HTML_tags_removed = re.sub(
                u'(\<(.+?)\>)+', "", str_internal_link_removed)
            str_external_link_removed = re.sub(
                u'(\[(.+?)\])+', "", str_HTML_tags_removed)
            str_lang_link_removed = re.sub(
                u'(\{\{(.+?)\}\})+', remove_lang_link,
                str_external_link_removed)
            basicInformationDict[m.group(1)] = str_lang_link_removed

# 辞書のitems()メソッドで全てのキー(key), 値(value)をたどる
# for/if文では文末のコロン「:」を忘れないように
for k, v in sorted(basicInformationDict.items(), key=lambda x: x[0]):
    print k.encode('utf_8'), v.encode('utf_8')
