import requests
import re
from bs4 import BeautifulSoup

'''
网络爬虫 豆瓣登录 这种方式已经过时了，针对豆瓣5.0的登录
目前豆瓣6.0中间嵌套了iframe 无法登录
'''
s = requests.Session()
url_login = 'https://accounts.douban.com/passport/login'

formdata = {
    'ck':'UPOy',
    'name': '674361437@qq.com',
    'password': '',
    'remember': 'false',

}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}

r = s.post(url_login, data=formdata, headers=headers)
content = r.text
soup = BeautifulSoup(content, 'html.parser')
captcha = soup.find('img', id = 'captcha_image')
print(content)
r = s.post(url_login, data = formdata, headers = headers)
if captcha:
    captcha_url = captcha['src']
    re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
    captcha_id = re.findall(re_captcha_id, content)
    print(captcha_id)
    print(captcha_url)
    captcha_text = input('Please input the captcha:')
    formdata['captcha-solution'] = captcha_text
    formdata['captcha-id'] = captcha_id
    r = s.post(url_login, data = formdata, headers = headers)
with open('contacts.txt', 'w+', encoding = 'utf-8') as f:
    f.write(r.text)

