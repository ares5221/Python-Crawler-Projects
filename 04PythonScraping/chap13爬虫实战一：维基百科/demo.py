#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
import re
import time

exist_url = []
news_ids = []
g_writecount = 0


def scrappy(url, depth=1):
    global g_writecount
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        r = requests.get("https://en.wikipedia.org/wiki/" + url, headers=headers)
        html = r.text
    except Exception as e:
        print('Failed downloading and saving', url)
        print(e)
        exist_url.append(url)
        return None

    exist_url.append(url)
    link_list = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>', html)
    unique_list = list(set(link_list) - set(exist_url))

    for eachone in unique_list:
        g_writecount += 1
        output = "No." + str(g_writecount) + "\t Depth:" + str(depth) + "\t" + url + ' -> ' + eachone + '\n'
        # print (output)
        with open('link_12-3.txt', "a+") as f:
            f.write(output)
            f.close()

        if depth < 2:
            scrappy(eachone, depth + 1)


scrappy("Wikipedia")
print(exist_url)