#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from selenium import webdriver

# option = webdriver.ChromeOptions()
# option.binary_location = r'C:\Windows.old\Users\12261\AppData\Local\Google\Chrome\Application\chrome.exe'
# driver = webdriver.Chrome()

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.set_page_load_timeout(10)
driver.get("http://www.santostang.com/2018/07/04/hello-world/")

comment = driver.find_element_by_css_selector('#list > div:nth-child(1) > div.reply-bottom > div.reply-content-wrapper > div.reply-content')
content = comment.find_element_by_tag_name('p')
print (content.text)