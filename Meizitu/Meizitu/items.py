# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituItem(scrapy.Item):
    img_name = scrapy.Field()  # 图集的名字
    img_link = scrapy.Field()  # 图集的url
    img_number = scrapy.Field()  #几张图片
    detail_img = scrapy.Field()  #url.jpg
    image_path = scrapy.Field()