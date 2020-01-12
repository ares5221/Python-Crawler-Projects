该项目用来展示scrapy框架爬取静态页面的demo操作
scrapy构建项目的步骤具体查看scrapy learning.md文件

demo02 爬取tencent招聘信息

该网站已经变成动态加载的方式了，无法用这种方式来抓取了，需要考虑直接抓包的方式

我们打算抓取：https://hr.tencent.com/position.php?&start=0#a 招聘岗位信息
首先进入03scrapy_demo路径
scrapy startproject Tencent

修改items.py

cd Tencent/spiders
scrapy genspider tencent "tencent.com"

编写tencent.py



编写pipelines.py在其中存储爬取结果

setting.py 启用管道
设置user agent

DEFAULT_REQUEST_HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}



