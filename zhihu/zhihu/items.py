# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()
    urlToken = scrapy.Field()
    isFollowed = scrapy.Field()
    avatarUrlTemplate = scrapy.Field()
    userType = scrapy.Field()
    answerCount = scrapy.Field()
    gender = scrapy.Field()
    followerCount = scrapy.Field()

