#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
session = requests.session()
import http.cookiejar as cookielib

post_url = 'http://www.santostang.com/wp-login.php'
agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers = {
    "Host": "www.santostang.com",
    "Origin":"http://www.santostang.com",
    "Referer":"http://www.santostang.com/wp-login.php",
    'User-Agent': agent
}
postdata = {
    'pwd': 'a12345',
    'log': 'test',
    'rememberme' : 'forever',
    'redirect_to': 'http://www.santostang.com/wp-admin/',
    'testcookie' : 1,
}

login_page = session.post(post_url, data=postdata, headers=headers)
print(login_page.status_code)
# session.cookies.save()

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")