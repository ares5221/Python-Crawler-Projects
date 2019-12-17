#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests

"""
info:
author:CriseLYJ
github:https://github.com/CriseLYJ/
update_time:2019-04-04
"""

"""
模拟登陆豆瓣
"""


class DouBanLogin(object):
    def __init__(self, account, password):
        self.url = "https://accounts.douban.com/j/mobile/login/basic"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        """初始化数据"""
        self.data = {
            "ck": "",
            "name": account,
            "password": password,
            "remember": "true",
            "ticket": ""
        }
        self.session = requests.Session()

    def get_cookie(self):
        """模拟登陆获取cookie"""
        html = self.session.post(
            url=self.url,
            headers=self.headers,
            data=self.data
        ).json()
        if html["status"] == "success":
            print("恭喜你，登陆成功")
        c = requests.cookies.RequestsCookieJar()  # 利用RequestsCookieJar获取
        c.set('cookie-name', 'cookie-value')
        self.session.cookies.update(c)
        print(self.session.cookies.get_dict())

    def get_user_data(self):
        """获取用户数据表明登陆成功"""
        # TODO: 这里填写你用户主页的url
        url = "http://www.douban.com/people/lovelqr/"
        # 获取用户信息页面
        html = self.session.get(url).content
        print(html)

    def run(self):
        """运行程序"""
        self.get_cookie()
        self.get_user_data()


if __name__ == '__main__':
    # account = input("请输入你的账号:")
    # password = input("请输入你的密码:")
    account = '674361437@qq.com'
    password = '674361437ljf5221'
    login = DouBanLogin(account, password)
    login.run()