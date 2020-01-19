#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
r = requests.get('http://www.santostang.com')
print (r.request.headers)


link = 'http://www.santostang.com'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers= headers)
print (r.request.headers)









