该项目用来展示scrapy框架爬取静态页面的demo操作
scrapy构建项目的步骤具体查看scrapy learning.md文件

demo03 爬取douyu 图片

我们打算抓取：http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20$offset=10
首先进入03scrapy_demo路径
scrapy startproject Douyu

修改items.py

cd Douyu/spiders
scrapy genspider douyu "douyucdn.cn"

编写douyu.py



编写pipelines.py在其中存储爬取结果
使用ImagesPipeline，
重写get_media_requests
item_completed

setting.py 启用管道
设置user agent 这里用手机的
IMAGES_STORE 必须手动添加




