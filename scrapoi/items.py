# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PoiItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
