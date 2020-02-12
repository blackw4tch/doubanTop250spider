# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class Doubantop250Item(scrapy.Item):
    title = scrapy.Field()
    cast = scrapy.Field()
    rate = scrapy.Field()
    number = scrapy.Field()
    quote = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
