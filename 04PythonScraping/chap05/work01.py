#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
link = 'https://beijing.anjuke.com/sale/'
r = requests.get(link, headers = headers)

soup = BeautifulSoup(r.text, 'lxml')
house_list = soup.find_all('li', class_="list-item")

count = 0
for house in house_list:
    name = house.find('div', class_ ='house-title').a.text.strip()
    room_num = house.find('div', class_='details-item').contents[1].text
    area = house.find('div', class_='details-item').contents[3].text
    floor = house.find('div', class_='details-item').contents[5].text
    year = house.find('div', class_='details-item').contents[7].text
    broker = house.find('span', class_='broker-name broker-text').text
    price = house.find('div', class_='pro-price').span.text
    address = house.find('span', class_='comm-address').text
    address = address.replace('\xa0\xa0\n','').replace(' ', '').replace('\n', '')
    tag_list = house.find_all('div', class_='tags-bottom')
    tags = [i.text.replace('\n', '') for i in tag_list]
    print (name, room_num, )
    print(area)
    print(floor)
    print(year)
    print(broker)
    print(price)
    print(address)
    print(tags)
    count +=1
    if count >20000:
        break
    print('---'*88)