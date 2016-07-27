# coding:utf-8
import json
import urllib2


def EnumKeys(data):
    for key in data.keys():
        print(key)
        if key == "imageinfo":
        	print data[key]
        	for i in data[key]:
        		print i.get('url')
        if isinstance(data[key], dict):
            EnumKeys(data[key])
        # else:
            #値の確認

url = 'https://commons.wikimedia.org/w/api.php?format=json&action=query&titles=File:Flag%20of%20the%20United%20Kingdom.svg&prop=imageinfo&&iiprop=url'
try:
    r = urllib2.urlopen(url)
    root = json.loads(r.read())
    query = root["query"]
    pages = query["pages"]


    EnumKeys(root)

finally:
    r.close()
