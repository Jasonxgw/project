# -*- coding: utf-8 -*-
import scrapy
import json
from zhihu.items import ZhihuItem
from scrapy_redis.spiders import RedisCrawlSpider
from selenium import webdriver




class ZhihuuserSpider(RedisCrawlSpider):
    name = 'zhihuusers'
    # allowed_domains = ['https://www.zhihu.com/']
    # start_urls = ['https://www.zhihu.com/people/excited-vczh/following']  # 他关注的人的list
    def start_requests(self):
        
        start = 'https://www.zhihu.com/people/excited-vczh/following'
        yield Request(url=start,callback=self.parse)

    def __int__(self):
        self.brow = webdriver.Chrome()

    def parse(self, response):
        if response.url == 302:
            self.brow.get(response.url)
        name_lists = response.xpath('//div[@id="data"]/@data-state').extract()
        n = json.loads(name_lists[0])
        items = n['entities']['users']
        base_url = 'https://www.zhihu.com/people/%s/following'
        item = ZhihuItem()
        for i in items:
            item['id'] = items[i]['id']  # 用户id
            item['name'] = items[i]['name']  # 用户name
            item['urlToken'] = items[i]['urlToken']  # 用户名
            item['isFollowed'] = items[i]['isFollowed']  # 是否被该用户关注
            item['avatarUrlTemplate'] = items[i]['avatarUrlTemplate']  # 头像url
            item['userType'] = items[i]['userType']  # 用户类型 people
            item['answerCount'] = items[i]['answerCount']  # 回答总数
            item['gender'] = items[i]['gender']  # 性别
            item['followerCount'] = items[i]['followerCount']  # 粉丝列表
            url = base_url % (item['urlToken'])
            yield scrapy.Request(url=url, callback=self.parse)
            yield item




