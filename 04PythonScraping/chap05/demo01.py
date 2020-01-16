#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re
m = re.match('www', 'www.santostang.com')
print ("匹配的结果:  ", m)
print ("匹配的起始与终点:  ", m.span())
print ("匹配的起始位置:  ", m.start())
print ("匹配的终点位置:  ", m.end())


line = "Fat cats are smarter than dogs, is it right?"
m = re.match( r'(.*) are (.*?) dogs', line)
print ('匹配的整句话', m.group(0))
print ('匹配的第一个结果', m.group(1))
print ('匹配的第二个结果', m.group(2))
print ('匹配的结果列表', m.groups())



import re
m_match = re.match('com', 'www.santostang.com')
m_search = re.search('com', 'www.santostang.com')
print (m_match)
print (m_search)

import re
m_match = re.match('[0-9]+', '12345 is the first number, 23456 is the sencond')
m_search = re.search('[0-9]+', 'The first number is 12345, 23456 is the sencond')
m_findall = re.findall('[0-9]+', '12345 is the first number, 23456 is the sencond')
print (m_match.group())
print (m_search.group())
print (m_findall)

import requests
import re

link = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers= headers)
html = r.text

title_list = re.findall('<h1 class="post-title"><a href=.*?>(.*?)</a></h1>',html)
print (title_list)














