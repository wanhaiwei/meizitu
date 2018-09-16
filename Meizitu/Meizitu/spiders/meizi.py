# -*- coding: utf-8 -*-
import scrapy
from Meizitu.items import MeizituItem

class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/']

    def parse(self, response):
        node_list = response.xpath("//ul[@id='pins']/li")
        for node in node_list:
            item = MeizituItem()
            item['img_name'] = node.xpath('./span/a/text()').extract_first()
            item['img_link'] = node.xpath('./span/a/@href').extract_first()
            # print(item['img_link'])
            yield scrapy.Request(url=item['img_link'], callback=self.detail_page,meta={"item": item})
        # yield scrapy.Request(url=)

    def detail_page(self, response):
        item = response.meta["item"]
        item["img_number"] = response.xpath('//div[@class="pagenavi"]/a[5]/span/text()').extract_first()  # 照片张数
        for i in range(1, int(item["img_number"]) + 1):
            # print(item["img_link"])
            yield scrapy.Request(url=item["img_link"] + '/'+str(i),callback=self.page_img,meta={"item": item})
        # print(type(item["img_number"]))

    def page_img(self,response):
        item = response.meta["item"]
        item['detail_img'] = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
        # print(all_img)
        yield item
