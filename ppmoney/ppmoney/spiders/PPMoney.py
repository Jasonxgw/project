# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from ppmoney.items import PpmoneyItem
from ppmoney.plates.plate import start_list

class PpmoneySpider(scrapy.Spider):
    name = 'PPMoney'
    start_urls = start_list

    def parse(self, response):
        base_url = 'https://bbs.ppmoney.com/'
        team = response.xpath('//*[@id="threadlisttableid"]/tbody')
        for i in team:
            Url = i.xpath('./tr/td[1]/a/@href').extract_first()  # 网页链接
            title = i.xpath('./tr/th/a[3]/text()').extract_first()  # 标题名
            auth = i.xpath('./tr/td[2]/cite/a/text()').extract_first()  # 作者名
            auth_url = i.xpath('./tr/td[2]/cite/a/@href').extract_first()  # 作者url
            time = i.xpath('./tr/td[2]/em/span/text()').extract_first()  # 作者更新时间
            back = i.xpath('./tr/td[3]/a/text()').extract_first()  # 回复
            wacth = i.xpath('./tr/td[3]/em/text()').extract_first()  # 查看
            speaker = i.xpath('./tr/td[4]/cite/a/text()').extract_first()  # 最后发表的用户
            speaker_time = i.xpath('./tr/td[4]/em/a/span/text()').extract_first()  # 最后发表的时间
            speaker_url = i.xpath('./tr/td[4]/em/a/@href').extract_first()  # 最后发表的作者的url
            try:  # url可能为空
                yield scrapy.Request(url='https://bbs.ppmoney.com/' + Url, callback=self.get_comment)
            except TypeError:
                pass

    # 获取用户评论
    def get_comment(self, response):
        item = PpmoneyItem()
        data = response.xpath('//*[@id="postlist"]/div/table')
        for i in range(len(data)):
            item['name'] = data[i].xpath('./tr[1]/td[1]/div/div[1]/div/a/text()').extract_first()  # 用户详细信息
            item['name_speak'] = str(data[i].xpath('./tr[1]/td[2]/div[2]/div/div[1]//text()').extract()).replace('\\r\\n','').strip('') # 评论主题
            yield item
