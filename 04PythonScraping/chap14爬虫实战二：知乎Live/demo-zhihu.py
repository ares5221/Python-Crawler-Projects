#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests

def scrapy(link):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    }
    r = requests.get(link, headers= headers)
    return (r.text)

link = "https://api.zhihu.com/lives/homefeed?includes=live"
html = scrapy(link)
print (html)