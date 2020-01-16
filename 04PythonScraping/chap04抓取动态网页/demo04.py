#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# 控制 css
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False

binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')
#把上述地址改成你电脑中Firefox程序的地址
fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.stylesheet",2)

driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps)
driver.get("http://www.santostang.com/2017/03/02/hello-world/")





# 限制图片的加载
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False
binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')
#把上述地址改成你电脑中Firefox程序的地址
fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.image",2)
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile = fp, capabilities=caps)
driver.get("http://www.santostang.com/2017/03/02/hello-world/")




# 限制 JavaScript 的执行
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False

binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')
#把上述地址改成你电脑中Firefox程序的地址
fp = webdriver.FirefoxProfile()
fp.set_preference("javascript.enabled", False)
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile = fp, capabilities=caps)
driver.get("http://www.santostang.com/2017/03/02/hello-world/")