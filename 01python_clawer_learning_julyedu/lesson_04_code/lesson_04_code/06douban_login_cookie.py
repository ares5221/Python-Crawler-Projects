import requests

url = 'https://www.douban.com/people/lovelqr/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}

# new_headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
# }

# 1先获取cookie
s = requests.Session()
print(s.cookies.get_dict())  # 先打印一下，此时一般应该是空的。
res = s.get(url, stream=True)
loginUrl = 'https://accounts.douban.com/j/mobile/login/basic'
postData = {'name': 'your username', 'password': 'your passwd', }
rs = s.post(loginUrl, postData, headers=headers)
print(rs.cookies)
# output: <RequestsCookieJar[<Cookie bid=D5ZCKg7mpFc for .douban.com/>, <Cookie dbcl2="46865330:V6si/adnss4" for .douban.com/>]>
c = requests.cookies.RequestsCookieJar()  # 利用RequestsCookieJar获取
c.set('cookie-name', 'cookie-value')
s.cookies.update(c)
print(s.cookies.get_dict())
#output: {'cookie-name': 'cookie-value', 'bid': 'D5ZCKg7mpFc', 'dbcl2': '"46865330:V6si/adnss4"'}

# 2 通过cookie来登录豆瓣个人页，get信息

cookies = {'bid': 'OlRUc0jhhvg', 'dbcl2': '"46865330:V6si/adnss4"'}
r = requests.get(url, cookies=cookies, headers=headers)
print(r.cookies)
# print(r.text)

with open('self_page.txt', 'wb+') as f:
    f.write(r.content)
