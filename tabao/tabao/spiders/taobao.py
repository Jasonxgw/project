# -*- coding: utf-8 -*-
import scrapy
import json
from tabao.items import TabaoItem
from urllib.parse import quote

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    # allowed_domains = ['https://s.taobao.com/search?q=%E5%A5%B3%E8%A3%85+%E8%A3%99']
    # start_urls = ['https://s.taobao.com/search?data-key=s&q=%E5%A5%B3%E8%A3%85+%E8%A3%99&ajax=true&ie=utf8&sort=sale-desc&p4ppushleft=%2C44&ntoffset=-6&s={}'.format(str((i-1)*44))for i in range(1,11)]
    url = 'https://s.taobao.com/search?data-key=s&q={}&ajax=true&ie=utf8&sort={}&p4ppushleft=%2C{}&ntoffset=-6&s={}'

    def start_requests(self):
        kewords = self.settings['KEYWORDS']
        keyword = quote(kewords, safe='').replace('%20', '+')
        url =  'https://s.taobao.com/search?data-key=s&q={}&ajax=true&ie=utf8&sort={}&p4ppushleft=%2C{}&ntoffset=-6&s={}'
        for i in range(self.settings['PAGE_COUNT']):
            url = self.url.format(keyword,self.settings['SORT'],self.settings['ONE_PAGE'],str(i*self.settings['ONE_PAGE']))
            yield scrapy.Request(url = url,callback=self.parse)


    def parse(self, response):
        item = TabaoItem()
        text = response.text
        json_test = json.loads(text)
        datas = json_test['mods']['itemlist']['data']['auctions']
        # datas1 = json_test['mods']['itemlist']['data']['auctions']['icon']['innerText'] #是否是金牌卖家
        for data in datas:
            item['raw_title'] = data['raw_title'] # 商品名
            item['nick'] = data['nick'] #店名
            item['view_price'] = data['view_price'] #价格
            item['view_sales'] = data['view_sales'] #收货人数
            item['item_loc'] = data['item_loc'] #发货地址
            item['detail_url'] = data['detail_url'] #详情链接
            yield item






