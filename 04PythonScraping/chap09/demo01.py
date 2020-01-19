#!/usr/bin/env python
# _*_ coding:utf-8 _*_

str1 = "我们"
print (str1)
print (type(str1))


str1 = "我们"
str_utf8 = str1.encode('utf-8')
print (str_utf8)
print (type(str_utf8))


str_decode = str1.encode('utf-8').decode('utf-8')
print (str_decode)
print (type(str_decode))

import chardet
str_gbk = "我们".encode('gbk')
print(chardet.detect(str_gbk))

# str_unicode_decode = "我们".decode()

# str_utf8 = "我们".encode('utf-8')
# str_gbk = str_utf8.encode('gbk')


str_utf8 = "我们".encode('utf-8')
str_gbk = str_utf8.decode('utf-8').encode('gbk')
print (str_gbk)












