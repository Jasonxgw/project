# -*- coding: utf-8 -*-
import scrapy
import json
from shixiseng.items import ShixisengItem

class ShixisengspiderSpider(scrapy.Spider):
    name = 'shixisengspider'
    # allowed_domains = ['https://www.shixiseng.com']

    # start_urls = ['https://www.shixiseng.com/interns?k=Python&p=%s'%(str(i)) for i in range(18)]

    def change_font(self):
        replace_dict = {"\ue02b": "0",
                        "\ue232": "1",
                        "\uecf3": "2",
                        "\ue553": "3",
                        "\uf005": "4",
                        "\ue4ec": "5",
                        "\uef28": "6",
                        "\uf386": "7",
                        "\uf78a": "8",
                        "\ue8e8": "9"
                        }
        for key, value in replace_dict.items():
            text = json.dumps(replace_dict).replace(key, value)

    def start_requests(self):
        base_url = 'https://www.shixiseng.com/interns?k=%s&p=%s'
        for i in range(self.settings['PAGE_COUNT']):
            url = base_url%(self.settings['QUERY_WORD'],str(i))
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        ul_xpaths = response.xpath('//*[@class="position-list-box"]/ul/li')
        ul_xpaths.xpath('./div[1]/div[1]/a/text()').extract_first() # 工作名称
        url = ul_xpaths.xpath('./div[1]/div[1]/a/@href').extract() # 详情页连接url
        ul_xpaths.xpath('./div[1]/div[1]/span/text()').extract_first() #距现在的发布时间

        ul_xpaths.xpath('./div[2]/div[1]/text()').extract_first() #工作地点
        ul_xpaths.xpath('./div[2]/div[2]/span[1]/text()').extract_first() #薪资/天
        ul_xpaths.xpath('./div[2]/div[2]/span[2]/text()').extract_first() #工作时间
        ul_xpaths.xpath('./div[2]/div[2]/span[3]/text()').extract_first() #实习多久
        for i in range(len(url)-1):
            detail_url = 'https://www.shixiseng.com'+url[i]
            yield scrapy.Request(url=detail_url,callback =self.parse_detail)


    def parse_detail(self,response):

        item = ShixisengItem()
        item['job_name'] = response.xpath('//div[@class="new_job_name"]/text()').extract_first()
        item['job_near_time'] = response.xpath('//div[@class="job_date "]/span[1]/text()').extract_first()  #*****
        item['job_saraly'] = response.xpath('//div/span[1]/text()').extract_first()  #*****
        item['job_address'] = response.xpath('//span[@class="job_position"]/text()').extract_first()  #*****
        item['job_academic'] = response.xpath('//span[@class="job_academic"]/text()').extract_first()  #*****
        item['job_day_week'] = response.xpath('//div/span[4]/text()').extract_first()  #*****
        item['job_time_count'] = response.xpath('//div[@class="job_msg"]/span[5]/text()').extract_first()  #*****
        item['job_good'] = response.xpath('//div[@class="job_good"]/text()').extract_first()  #*****

        a = response.xpath('//div[@class="job_part"]/div/p').extract()  #*****

        item['job_desc'] = str(a).replace('<br>', '\n').replace('<p></p>','')

        return item


