# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AreaItem(scrapy.Item):
    # define the fields for your item here like:

    # 城市
    city = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # AQI
    AQI = scrapy.Field()
    # 质量等级
    QCL = scrapy.Field()
    # PM2.5
    PM = scrapy.Field()
    # PM10
    PM10 = scrapy.Field()
    # SO2
    SO2 = scrapy.Field()
    # CO
    CO = scrapy.Field()
    # NO2
    NO2 = scrapy.Field()
    # O3_8H
    O3_8h = scrapy.Field()

