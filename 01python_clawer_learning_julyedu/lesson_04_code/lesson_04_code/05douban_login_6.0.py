#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
from selenium import webdriver
import time

username = 'username'
password = 'pass'

driver = webdriver.Chrome(executable_path=r'G:\pythonLearningWorkSpace\Python-Crawler-Projects\01python_clawer_learning_julyedu\lesson_03_code\lesson_03_code\chromedriver.exe')
driver.get('https://www.douban.com/')
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(iframe)
driver.find_element_by_class_name('account-tab-account').click()
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_class_name('btn-account').click()
time.sleep(5)
driver.quit()