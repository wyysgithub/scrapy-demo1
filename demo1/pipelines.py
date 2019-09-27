# -*- coding: utf-8 -*-
import pymongo
from demo1.settings import mongo_db_collection, mongo_db_name, mongo_host, mongo_port


# Define your item pipelines here
#  使用该文件需要在setting里面激活
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Demo1Pipeline(object):

    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
