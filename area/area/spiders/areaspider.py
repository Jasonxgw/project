# -*- coding: utf-8 -*-
import scrapy
from area.items import AreaItem

class AreaSpiderSpider(scrapy.Spider):
    name = 'area_spider'
    # allowed_domains = ['www.aqistudy.cn']
    base_url = 'https:/www.aqistudy.cn/historydata/'
    start_urls = [base_url]

    def parse(self, response):
        tops_citys = response.xpath('//div[@class="bottom"]/ul[@class="unstyled"]/li/a/text()').extract()[1:2] # 热门城市
        tops_urls = response.xpath('//div[@class="bottom"]/ul[@class="unstyled"]/li/a/@href').extract()[1:2]  # 热门城市url
        # alls_citys = response.xpath('/div[@class="all"]/div[2]/ul[@class="unstyled"]/div[2]/li/a/text()').extract() # 全部城市
        # alls_urls = response.xpath('/div[@class="all"]/div[2]/ul[@class="unstyled"]/div[2]/li/a/@href').extract() # 全部城市url
        for city,Url in zip(tops_citys,tops_urls):
            url = self.base_url+Url
            yield scrapy.Request(url=url,meta={'city':city},callback=self.parse_mouth)

    def parse_mouth(self,response):
        print('正在搜索详细月份..')
        mouth_urls = response.xpath('//td[1]/a/@href').extract()[0:2]#爬取一条数据先
        for i in mouth_urls:
            url = self.base_url+i
            yield scrapy.Request(url = url,meta ={'city':response.meta['city']},callback=self.parse_day)

    def parse_day(self,response):
        print('正在搜索详细月数据..')
        item = AreaItem()
        mouths = response.xpath('//tr')
        mouths.pop(0)
        for i in mouths:
            item['city'] = response.meta['city']
            item['date'] =i.xpath('./td[1]/text()').extract_first()
            item['AQI'] =i.xpath('./td[2]/text()').extract_first()
            item['QCL'] =i.xpath('./td[3]/span/text()').extract_first()
            item['PM'] =i.xpath('./td[4]/text()').extract_first()
            item['PM10'] =i.xpath('./td[5]/text()').extract_first()
            item['SO2'] =i.xpath('./td[6]/text()').extract_first()
            item['CO'] =i.xpath('./td[7]/text()').extract_first()
            item['NO2'] =i.xpath('./td[8]/text()').extract_first()
            item['O3_8h'] =i.xpath('./td[9]/text()').extract_first()
            yield item




