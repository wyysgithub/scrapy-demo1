# -*- coding: utf-8 -*-
import pymysql.cursors
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from douban.settings import MYSQL_CHARSET, MYSQL_DB, MYSQL_HOST, MYSQL_PORT, MYSQL_PWORD, MYSQL_UNAME


class DoubanPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            db=MYSQL_DB,
            user=MYSQL_UNAME,
            passwd=MYSQL_PWORD,
            charset=MYSQL_CHARSET,
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """insert into douban (mIndex,title,star,digest,quote,imgSrc,doubanHref) values (%s,%s,%s,%s,%s,%s,%s)""",
                (item['index'], item['title'], item['star'], item['digest'], item['quote'], item['imgSrc'], item['doubanHref']))

            self.connect.commit()
        except Exception as error:
            print(error)

        return item
