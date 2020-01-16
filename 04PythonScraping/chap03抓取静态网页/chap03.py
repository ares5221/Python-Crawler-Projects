#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
r = requests.get('http://www.santostang.com/')
print ("文本编码:", r.encoding)
print ("响应状态码:", r.status_code)
# print ("字符串方式的响应体:", r.text)


import requests
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
'Host': 'www.santostang.com'
}
r = requests.get('http://www.santostang.com/', headers=headers)
print ("响应状态码:", r.status_code)