#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re
str1 = '你好$$$我正在学Python@#@#现在需要&%&%&修改字符串'
str2 = re.sub('[$@#&%]+', ' ' ,str1)
print (str2)

for i in range(1, 10):
    for j in range(1, i+1):
        print ("%dx%d=%d\t" % (j, i, i*j), end="")
    print("")


a = 1
def fun(a):
    a = 2
    print('inner a', a)
fun(a)
print ('outer a',a)


a = []
def fun(a):
    a.append(1)
fun(a)
print (a)


class Person:
    name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"
print (p1.name)
print (p2.name)
print (Person.name)


class Person:
    name=[]

p1=Person()
p2=Person()
p1.name.append(1)
print (p1.name)
print (p2.name)
print (Person.name)


def calcute_profit(I):
    arr = [1000000,600000,400000,200000,100000,0] #这应该就是各个分界值了，把它们放在列表里方便访问
    rat = [0.01,0.015,0.03,0.05,0.075,0.1] #这是各个分界值所对应的奖金比例值
    r = 0                       #这是总奖金的初始值
    for idx in range(0,6):      #有6个分界值当然要循环6次
        if I > arr[idx]:
            r = r + (I - arr[idx]) * rat[idx]
            I = arr[idx]
    return r

I = int(input('净利润:'))
profit = calcute_profit(I)
print ('利润为%d元时，应发奖金总数为%d元' % (I, profit))

'''
def calcute_profit(I):
    I = I / 10000
    if I <= 10:
        a = I * 0.01
        return a * 10000
    elif I <= 20 and I > 10:
        b = 0.25 + I * 0.075
        return b * 10000
    elif I <= 40 and I > 20:
        c = 0.75 + I * 0.05
        return c * 10000
    elif I <= 60 and I > 40:
        d = 0.95 + I * 0.03
        return d * 10000
    elif I <= 60 and I > 100:
        e = 2 + I * 0.015
        return e * 10000
    else:
        f = 2.95 + I * 0.01
        return f * 10000


I = int(input('净利润:'))
profit = calcute_profit(I)
print('利润为%d元时，应发奖金总数为%d元' % (I, profit))
'''