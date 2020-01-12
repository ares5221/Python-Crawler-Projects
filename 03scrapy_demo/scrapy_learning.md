scrapy 构建步骤
1，创建项目  scrapy startproject xxx :新建一个新的爬虫项目
2，明确目标  编写items.py :明确要抓取的目标
3，制作爬虫  spiders/xxspider.py :制作爬虫开始爬取网页
4，存储内容  pipelines.py :设计管道存储爬取内容



step01:
创建爬虫项目
scrapy startproject ITcast

step02
制作爬虫，可以制作多个爬虫，设置不同name区分
后面接的是允许爬取的地址域
cd ITcast/spiders
scrapy genspider itcast "http://www.itcast.cn"

step03
编写items.py 明确要提取的数据

step04
编写spiders/xxx.py 编写爬虫文件，处理请求和相应，
在pares方法中直接print(response.body)
主要是重写pares方法，在其中提取数据将数据保存在items（）实例对象中，以及yield item

step05
编写pipelines.py 编写管道文件，处理spider返回item数据
比如本地持久化存储或存储数据库

step06
编写setting.py 启动管道组件，ITEM_PIPELINES = {} 以及其他相关设置


step07
在spiders路径下，输入scrapy发现出现的内容和原来不一样，多了check crawl等

执行爬虫开始爬取，使用crawl方法 后接爬虫name itcast
scrapy crawl itcast

