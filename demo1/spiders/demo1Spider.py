import scrapy
from demo1.items import Demo1Item


class demoSpider(scrapy.Spider):
    # 爬虫名
    name = "demo1"
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    # 数据解析 默认解析方法
    def parse(self, response):
        # 循环电影的条目
        movieList = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        # filename = 'baike-%s.html' % page
        for i in movieList:
            # items 文件导入进来
            demo_item = Demo1Item()
            # 详细的xpath规则
            demo_item['index'] = i.xpath(".//div[@class='item']//em/text()").extract_first()
            demo_item['name'] = i.xpath(".//div[@class='item']//div[@class='hd']//span/text()").extract_first()
            demo_item['star'] = i.xpath(".//span[@class='rating_num']/text()").extract_first()
            # 拿到数据之后做处理
            content = i.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            for c in content:
                content_s = "".join(c.split())
                demo_item['introduce'] = content_s

            # 把所有数据放入管道
            yield demo_item
            print(demo_item)

        # 解析下一页的规则
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            # 执行完成之后，会执行回调函数，这时候已经是第二页的url了
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)
