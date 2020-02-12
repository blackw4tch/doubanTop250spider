# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.spiders import Request
class SavemoviesPipeline(object):
    def creat_dir(self,path):
        os.makedirs(path)
    def process_item(self,item,spider):
        apath = "./movies/" + item["title"]
        self.creat_dir(apath)
        text = apath + "/" +item["title"] + '.txt'
        f = open(text, 'wb')
        f.write(("电影名:"+item["title"]+'\n'+"评分:"+item["rate"]+"  "+item["number"]+'\n'+"演职员:"
                +item["cast"]+'\n'+item["quote"]).encode('utf-8'))
        f.close()
        return item
class SaveImagePipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        return [Request(x, meta={"title": item["title"]}) for x in item.get(self.images_urls_field, [])]
    def file_path(self,request,response=None,info=None):
        title = request.meta["title"]
        image_name = request.meta["title"]+".jpg"
        return "%s/%s" % (title, image_name)














