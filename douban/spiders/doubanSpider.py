import scrapy
from douban.items import DoubanItem


class doubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        # xpath返回的是一个SelectorList对象实例
        movie_list = response.xpath("//div[@class='article']/ol[@class='grid_view']//li")
        for m in movie_list:
            douban_item = DoubanItem()
            # 使用extract或者get可以获得字符串
            # 区别：对于Selector类型的对象，并不能使用extract_first()方法，而使用get()可以
            douban_item['index'] = m.xpath(".//div[@class='item']/div[@class='pic']/em/text()").get()
            douban_item['title'] = m.xpath(".//div[@class='item']/div[@class='info']/div[@class='hd']/a/span[@class='title']/text()").get()
            douban_item['star'] = m.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").get()
            _digest = m.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/p[1]/text()").getall()
            for d in _digest:
                _digest_result = "".join(d.split())
                douban_item['digest'] = _digest_result

            douban_item['quote'] = m.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/p[@class='quote']/span[@class='inq']/text()").get()
            douban_item['imgSrc'] = m.xpath(".//div[@class='item']/div[@class='pic']/a/img/@src").get()
            douban_item['doubanHref'] = m.xpath(".//div[@class='item']/div[@class='info']/div[@class='hd']/a/@href").get()

            yield douban_item

            next_link = response.xpath("//span[@class='next']/link/@href").getall()
            if next_link:
                next_link = next_link[0]
                yield scrapy.Request("https://movie.douban.com/top250" + next_link,callback=self.parse)