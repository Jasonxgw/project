# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import os
from scrapy.exceptions import DropItem
from pybloom import BloomFilter

class BloomCheckPipeline(object):
    def __int__(self):
        file_name = 'bloomfilter'

    def open_spider(self, spider):
        file_name = 'bloomfilter'
        is_exist = os.path.exists(file_name + '.blm')
        if is_exist:
            self.bf = BloomFilter.fromfile(open('bloomfilter.blm', 'rb'))
            print('open blm file success')
        else:
            self.bf = BloomFilter(100000, 0.001)
            print('didn\'t find the blm file')

    def process_item(self, item, spider):
        # 我是过滤掉相同url的item 各位看需求
        if item['urlToken'] or item['id'] in self.bf:
            print('drop one item for exist')
            raise DropItem('drop an item for exist')
        else:
            self.bf.add(item['urlToken'])
            print('add one success')
            return item

    def close_spider(self, spider):
        self.bf.tofile(open('bloomfilter.blm', 'wb'))


class ZhihuPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    collection_name = 'zhuhuus'  # 表名名称

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        # 必须在settings中 配置 MONGO_URI 和 MONGO_DATABASE
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')  # items 是默认值
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
