import requests
from lxml import etree
from bs4 import BeautifulSoup

headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

for id in range(0, 1,1):
    url = 'https://movie.douban.com/top250/?start-' + str(id)
    r = requests.get(url, headers=headers)
    print(r.text)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup)
    items = soup.find_all('ol', class_='grid_view')
    # items = root.xpath('//*[@id="content"]/div/div[1]/div[1]')
    print(len(items))
    for item in items:
        title = item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
        name = title[0].encode('gb2312', 'ignore').decode('gb2312')
        # rank = item.xpath('./div[@class="pic"]/em/text()')[0]
        rating = item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
        print(name, rating)
