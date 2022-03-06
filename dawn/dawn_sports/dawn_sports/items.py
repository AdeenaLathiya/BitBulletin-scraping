# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DawnSportsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    title = scrapy.Field()
    author = scrapy.Field()
    article = scrapy.Field()
    picture = scrapy.Field()
    time = scrapy.Field()
    date = scrapy.Field()

    pass
