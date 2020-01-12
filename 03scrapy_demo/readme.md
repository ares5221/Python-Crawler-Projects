该项目用来展示scrapy框架爬取静态页面的demo操作
scrapy构建项目的步骤具体查看scrapy learning.md文件

demo01 爬取itcast讲师信息
我们打算抓取：http://www.itcast.cn/channel/teacher.shtml 网站里的所有讲师的姓名、职称和个人信息。
首先进入03scrapy_demo路径
scrapy startproject ITcastSpider

修改items.py

cd ITcast/spiders
scrapy genspider itcastspider "www.itcast.cn"

编写itcastspider.py
完成后 可以使用下面四种方式直接命令行输出结果，一般输出json csv
# json格式，默认为Unicode编码
scrapy crawl itcast -o teachers.json

# json lines格式，默认为Unicode编码
scrapy crawl itcast -o teachers.jsonl

# csv 逗号表达式，可用Excel打开
scrapy crawl itcast -o teachers.csv

# xml格式
scrapy crawl itcast -o teachers.xml


编写pipelines.py在其中存储爬取结果

setting.py 启用管道


