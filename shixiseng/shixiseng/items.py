# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShixisengItem(scrapy.Item):
    # define the fields for your item here like:
    job_name = scrapy.Field() #工作名称
    job_near_time = scrapy.Field() # 最近时间
    job_saraly = scrapy.Field()  #工作价格 每天
    job_address = scrapy.Field() #工作地址
    job_academic = scrapy.Field() # 工作经验
    job_day_week = scrapy.Field() #每周工作几天
    job_time_count = scrapy.Field() #实习多久
    job_good = scrapy.Field() # 职位诱惑


    job_desc = scrapy.Field() #职位描述


    company_name = scrapy.Field() #公司名称
    company_peoper = scrapy.Field() #公司人数
    company_direction = scrapy.Field() #公司方向
    company_address = scrapy.Field() #公司地址
    company_network = scrapy.Field() #公司网站

    end_time = scrapy.Field()# 截止时间





