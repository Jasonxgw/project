# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    new_chapter = scrapy.Field()
    auth = scrapy.Field()
    words = scrapy.Field()
    last_time = scrapy.Field()
    status = scrapy.Field()
