# jandan_spider
使用selenium爬取煎蛋妹纸图片(Python3)

这里是一个简单的例子，使用类似的套路可以处理大量此类网站，希望对爬虫新手有一点借鉴作用。

#### 简介
在脚本中输入煎蛋妹子首页网址'https://jandan.net/ooxx'，
脚本将自动补全网址，并下载煎蛋妹子全站图片。

之所以使用selenium是因为，煎蛋妹子原始图片url不出现在网页原始代码中，但可在chrome开发者工具中的Elements选项卡中查看，而`webdriver.Chrome().get(url_base)`可以轻松获取这些url。


#### 准备工作
测试前请安装好selenium，如果运行显示chrome版本不匹配，可以自行下载chrome drive，
然后替换该路径下文件，也可以放在别的路径下，使用参数指定
webdriver.Chrome(executable_path="G:/Download/AutoCrowerByKeyWords/data/drive/chromedriver.exe")
并在spider_jandan.py当前路径新建img文件夹
```
/root
    /img
    chromedriver.exe
    spider_jandan.py
    README.md
```
然后执行`python spider_jandan.py`，所有图片将保存在img文件夹中。
