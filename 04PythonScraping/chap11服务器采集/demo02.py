#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
import time
import random
import changeIP

link = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

def scrapy(url, num_try = 3):
    try:
        r = requests.get(url, headers= headers)
        html = r.text
        time.sleep(random.randint(0,2)+random.random())
    except Exception as e:
        print (e)
        html = None
        if num_try >0:
            x = changeIP.adsl()
            x.reconnect()
            html = scrapy(url, num_try-1)
    return html

result = scrapy(link)