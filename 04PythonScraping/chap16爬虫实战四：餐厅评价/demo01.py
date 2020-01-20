#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.dianping.com/search/category/7/10/p1")

from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False

binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')
# 把上述地址改成你电脑中Firefox程序的地址
fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.image", 2)
fp.set_preference("javascript.enabled", False)

driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps)
driver.implicitly_wait(30)

with open('restaurant_list.csv', encoding='utf-8') as f:
    csv_file = csv.reader(f)
    link_list = [[row[1], row[2]] for row in csv_file]

for eachone in link_list:
    name = eachone[0]
    link = eachone[1]
    output_list = []
    driver.get(link)
    locator = (By.CLASS_NAME, 'content')
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))

    soup = BeautifulSoup(driver.page_source, "lxml")

    dishes_list = []
    for eachone in soup.find(class_="recommend-name"):
        try:
            dishes = eachone['title'].strip() + eachone.em.text
            dishes_list.append(dishes)
        except:
            pass

    comment_list = []
    for eachone in soup.find(class_="content"):
        try:
            comment_tag = eachone.a.text
            comment_list.append(comment_tag)
        except:
            pass

    output_list.append([name, link, '|'.join(dishes_list), '|'.join(comment_list)])
    with open('restuarant_detail.csv', 'a+', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        writer.writerows(output_list)
    time.sleep(2)