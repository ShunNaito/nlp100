# coding:utf-8
import json
import re
import urllib2
import urllib


def EnumKeys(data):
    for key in data.keys():
        if key == "imageinfo":
            for i in data[key]:
                print i.get('url')
        if isinstance(data[key], dict):
            EnumKeys(data[key])

urlprefix = 'https://commons.wikimedia.org/w/api.php?'

query = {'format': 'json',
         'action': 'query',
         'prop': 'imageinfo'}

parameter = {
    'iiprop': 'url'
}

r = re.compile('\|.+?=\s(.+)')

f = open('jawiki-country.json', 'r')
lines = f.readlines()
f.close()

for line in lines:
    article_dict = json.loads(line)
    if article_dict["title"] == u"イギリス":
        England_text = article_dict["text"]

lines = England_text.split("\n")
for line in lines:
    if u"国旗画像" in line:
        page = {'titles': 'File:' + r.search(line).group(1).encode('utf_8')}
        query.update(page)
        url = urlprefix + urllib.urlencode(query) + '&' \
            + urllib.urlencode(parameter)
        try:
            r = urllib2.urlopen(url)
            root = json.loads(r.read())
            query = root["query"]
            pages = query["pages"]
            EnumKeys(root)
        finally:
            r.close()
