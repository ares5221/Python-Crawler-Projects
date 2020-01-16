#!/usr/bin/env python
# _*_ coding:utf-8 _*_



import requests
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
'Host': 'www.santostang.com'
}
r = requests.get('http://www.santostang.com/', headers=headers)
print ("响应状态码:", r.status_code)


import requests
key_dict = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=key_dict)
print (r.text)