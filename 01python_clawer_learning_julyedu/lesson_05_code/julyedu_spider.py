

import scrapy


class JulyeduSpider(scrapy.Spider):
    name = "julyedu"
    start_urls = [
        'http://www.julyedu.com/category/index',
    ]

    def parse(self, response):
        print('@@@@@@@@@@@@@@@@@@@')
        print(response)
        for julyedu_class in response.css('#course > div > div.content > div:nth-child(3) > a:nth-child(1) > div.course-dec > div.course-title'):
            print(julyedu_class)
            print('ssss')
            print (julyedu_class.css('a'))
            # print julyedu_class.xpath('a/p[@class="course-info-tip"][1]/text()').extract_first()
            # print julyedu_class.xpath('a/p[@class="course-info-tip"][2]/text()').extract_first()
            # print response.urljoin(julyedu_class.xpath('a/img[1]/@src').extract_first())
            # print "\n"

            # yield {
            #     'title':julyedu_class.xpath('a/h4/text()').extract_first(),
            #     'desc': julyedu_class.xpath('a/p[@class="course-info-tip"][1]/text()').extract_first(),
            #     'time': julyedu_class.xpath('a/p[@class="course-info-tip"][2]/text()').extract_first(),
            #     'img_url': response.urljoin(julyedu_class.xpath('a/img[1]/@src').extract_first())
            # }


# run
# scrapy runspider julyedu_spider.py -o julyedu_class.jspn