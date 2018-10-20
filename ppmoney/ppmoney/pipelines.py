# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo



class PPMoneyMongoPipeline(object):
    def open_spider(self,spider):
        self.client = pymongo.MongoClient("127.0.0.1",27017)
        self.db = self.client['PPMoney']
        self.collection = self.db['ppmoney']

    def process_item(self,item,spider):
        self.collection.insert(dict(item))
        return item
