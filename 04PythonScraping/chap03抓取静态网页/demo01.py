#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
key_dict = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=key_dict)
print ("URL已经正确编码:", r.url)
print ("字符串方式的响应体: \n", r.text)