# -*- coding: utf-8 -*-
"""
This is a simple python spider experiment based on selenium.webdriver.
I choose selenium because the image urls can be find in the `Elements`
table of Chrome, however, the image urls are missing in the  source
code page. The good news is that it is pretty easy to get the image urls
by using `webdriver.Chrome().get(url_base)`.
煎蛋网爬虫

"""
import os
import time
import requests
import random
from selenium import webdriver
import uuid

# 计时器
def timeit(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'time consuming: {(end - start):.4f} seconds. ({func})')
    return wrapper


def download_pic(img_url):
    r = requests.get(img_url, stream=True)
    image_name = img_url.split('/')[-1]
    print(image_name)
    image_name = str(uuid.uuid1()) + image_name
    print('ss', image_name)
    cur_dir = os.path.abspath(os.curdir)
    img_dir = os.path.join(cur_dir, 'img', image_name)
    if not os.path.exists(img_dir):
        # 下列方式适合较大文件下载
        with open(img_dir, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print(f'{image_name} is saved.')


# 生成每个图片的url
def generate_urls(url_base, browser):
    """from the `url_base` to the real url: http://jandan.net/ooxx/=58#comments"""
    cur_page_id = 1  # asign a value, but it will be changed
    ls = browser.find_elements_by_class_name('current-comment-page')  # .click()
    for idx, ele in enumerate(ls):
        print(f'ls_{idx}: {ele.text} ---> {ele.text[1:-1]}')  # ele.text: [59]
        cur_page_id = int(ele.text[1:-1])
    all_page_ids = [i + 1 for i in range(cur_page_id + 1)]
    all_page_ids_reversed = all_page_ids[::-1]
    url_ls = [url_base + '/' + str(id_) + '=#comments' for id_ in all_page_ids_reversed]
    return url_ls


@timeit
def main():
    """download all of the raw pictures for all pages, e.g. page 1 ~ page 60"""
    url_base = 'https://jandan.net/ooxx'
    browser = webdriver.Chrome()
    browser.get(url_base)  # 能够获取chrome开发者模式中的Element内部内容
    # generate the page ids for all pages
    url_ls = generate_urls(url_base, browser)  # list
    for idx, url_ in enumerate(url_ls):
        print(f'the {idx}th page starts (url:{url_})')
        browser.get(url_)  # 能够获取chrome开发者模式中的Element内部内容
        ls = browser.find_elements_by_partial_link_text('[查看原图]')  # .click()
        img_urls = []
        for idx, ele in enumerate(ls):
            img_url = ele.get_attribute("href")
            img_urls.append(img_url)
            print(f'ls_{idx}: {ele.get_attribute("href")}')  # ele.text: [查看原图]
            download_pic(img_url)
            # TODO: 20180506: 图片名应该不会冲突，但是加上随机数应该更加保险一些

        time.sleep(1 + random.random())

    browser.get_screenshot_as_file("capture.png")
    browser.close()


if __name__ == "__main__":
    main()
