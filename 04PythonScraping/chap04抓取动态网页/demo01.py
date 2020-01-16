#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests

link = "https://api-zero.livere.com/v1/comments/list?callback=jQuery1124049866736766120545_1506309304525&limit=10&offset=1&repSeq=3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1506309304527"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

r = requests.get(link, headers= headers)
print (r.text)

# 获取 json 的 string
json_string = r.text
json_string = json_string[json_string.find('{'):-2]

import json
json_data = json.loads(json_string)
comment_list = json_data['results']['parents']

for eachone in comment_list:
    message = eachone['content']
    print (message)