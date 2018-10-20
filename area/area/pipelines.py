# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
import redis
from datetime import datetime
from scrapy.exporters import CsvItemExporter

class AreaPipeline(object):
    def process_item(self, item, spider):
        item['source'] = spider.name
        item['utc_time'] = str(datetime.utcnow())
        return item

# 可以使用

class AreaJsonPipeline(object):
    def open_spider(self, spider):
        self.filename = open("area.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        self.filename.write(content)
        return item

    def close_spider(self, spider):
        self.filename.close()

# 可以使用
class AreaMongoPipeline(object):
    def open_spider(self,spider):
        self.client = pymongo.MongoClient("127.0.0.1",27017)
        self.db = self.client['areas']
        self.collection = self.db['area']

    def process_item(self,item,spider):
        self.collection.insert(dict(item))
        return item

import redis
from scrapy import Item

class RedisPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        db_host = spider.settings.get('REDIS_HOST', 'localhost')
        db_port = spider.settings.get('REDIS_PORT', 6379)
        db_index = spider.settings.get('REDIS_DB_INDEX', 'db0')####修改
        db_passwd = spider.settings.get('REDIS_DB_PASSWD', 'myredisservice')

        self.db_conn = redis.StrictRedis(host=db_host, port=db_port, db=db_index,password=db_passwd)
        self.item_i = 0

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.connection_pool.disconnect()

    # 处理数据
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    # 插入数据
    def insert_db(self, item):
        if isinstance(item, Item):
            item = dict(item)

        self.item_i += 1
        self.db_conn.hmset('data:{}'.format(self.item_i), item)



# #爬取到的数据写入到MySQL数据库
class DBPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            # 查重处理
            self.cursor.execute(
                """select * from doubanmovie where img_url = %s""",
                item['img_url'])
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # 重复
            if repetition:
                pass

            else:
                # 插入数据
                self.cursor.execute(
                    """insert into doubanmovie(city, date, AQI, QCL ,PM, PM10,SO2,CO,NO2,O3_8h)
                    value (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)""",
                        item['city'],
                        item['date'],
                        item['AQI'],
                        item['QCL'],
                        item['PM'],
                        item['PM10'],
                        item['SO2'],
                        item['CO'],
                        item['NO2'],
                        item['O3_8h'],
                    )

            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            log(error)
        return item
import pymysql
class MySQLPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME','mysql1')### 要修改
        host = spider.settings.get('MYSQL_HOST', 'localhost')### 要修改
        port = spider.settings.get('MYSQL_PORT', 3306)### 要修改
        user = spider.settings.get('MYSQL_USER', 'root')### 要修改
        passwd = spider.settings.get('MYSQL_PASSWORD', '12345')### 要修改

        self.db_conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        values = ( #  ### 要修改
            item['city'],
            item['date'],
            item['AQI'],
            item['QCL'],
            item['PM'],
            item['PM10'],
            item['SO2'],
            item['CO'],
            item['NO2'],
            item['O3_8h'],
        )

        sql = '''INSERT INTO mysql1(city,date,AQI,QCL,PM,PM10,SO2,CO,NO2,O3_8h,) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''###要修改
        self.db_cur.execute(sql, values)


import csv
class CSVPipeline(object):

   def __init__(self):
      self.csvwriter = csv.writer(open('items.csv', 'a'), delimiter=',')
      self.csvwriter.writerow(['城市','日期','AQI','QCL(质量)','PM','PM10','SO2','CO','NO2','O3_8h'])

   def process_item(self, item, ampa):


      self.csvwriter.writerow([item['city'],item['date'],item['AQI'],item['PM'],item['PM10'],item['SO2'],item['CO'],item['NO2'],item['O3_8h']])


      return item