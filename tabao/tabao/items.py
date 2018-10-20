# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TabaoItem(scrapy.Item):
    # define the fields for your item here like:
    raw_title = scrapy.Field()
    view_price = scrapy.Field()
    view_sales = scrapy.Field()
    item_loc = scrapy.Field()
    nick = scrapy.Field()
    detail_url = scrapy.Field()

