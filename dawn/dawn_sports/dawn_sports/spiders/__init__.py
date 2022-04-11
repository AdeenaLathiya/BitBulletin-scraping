# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

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

class DawnTechItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title2 = scrapy.Field()
    author2 = scrapy.Field()
    article2 = scrapy.Field()
    picture2 = scrapy.Field()
    # time = scrapy.Field()
    date2 = scrapy.Field()

    pass
