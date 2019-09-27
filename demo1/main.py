from scrapy import cmdline
# cmdline.execute("scrapy crawl demo1".split())

# 执行并保存为json文件
cmdline.execute("scrapy crawl demo1 -o data.json".split())