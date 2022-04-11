# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# from unicodedata import category
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
    category = scrapy.Field()

    pass

class DawnTechItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title2 = scrapy.Field()
    author2 = scrapy.Field()
    article2 = scrapy.Field()
    picture2 = scrapy.Field()
    # time = scrapy.Field()
    date2 = scrapy.Field()
    category2 = scrapy.Field()

    pass
