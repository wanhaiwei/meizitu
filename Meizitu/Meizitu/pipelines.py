# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import scrapy

from scrapy.pipelines.images import ImagesPipeline
from Meizitu.settings import IMAGES_STORE

from scrapy.exceptions import DropItem


class ImgPipeline(ImagesPipeline):

    # def get_media_requests(self, item, info):
    #
    #     for i in range(int(item['img_number'])):
    #         image_link = item['img_link'] + '/' + str(i)
    #         # 发送图片的请求。响应会保存在setting里指定的路径
    #         print(image_link)
    #
    #         yield scrapy.Request(url=image_link)

    def get_media_requests(self, item, info):
        # 获取item数据的图片链接
        image_link = item['detail_img']
        # 发送图片的请求。响应会保存在setting里指定的路径
        yield scrapy.Request(url=image_link)

    def item_completed(self, results, item, info):
        # print(os.getcwd())
        # print(results)
        # os.chdir(IMAGES_STORE)
        if not os.path.exists('./{}'.format(item["img_name"])):
            self.file_name = os.mkdir('./{}'.format(item["img_name"]))
        image_paths = [x['path'] for ok, x in results if ok]
        old_path = IMAGES_STORE + '/' + image_paths[0]
        # print(old_path + "===========================")
        new_path = IMAGES_STORE + '/' + item["detail_img"][-9:-5] + '.jpg'
        item['detail_img'] = new_path
        print(new_path)
        try:
            os.rename(old_path,new_path)

        except:
            print('已修改...')
        # print(new_path)
        # shutil.move(old_path, new_path)
        return item


        # old_path = IMAGES_STORE + results[1]['path']
        # new_path = IMAGES_STORE + item["img_name"]
        # os.rename(old_path, new_path)
        # 每个result表示一个图片信息，
        # image_path = [x['path'] for ok, x in results if ok]
        # old_name = IMAGES_STORE + image_path[0]
        # new_name = IMAGES_STORE + item['img_name'][0:5] + '.jpg'
        # item['img_name'] = new_name

        # try:
        #     # 修改名字
        #     os.rename(old_name, new_name)
        # except:
        #     print("图片已被修改。。。。")


class MeizituPipeline(object):
    def open_spider(self, spider):
        self.file = open('meizitu.json', 'w+', encoding='utf-8')

    def process_item(self, item, spider):
        data = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(data)
        return item

    def close_spider(self, spider):
        self.file.close()