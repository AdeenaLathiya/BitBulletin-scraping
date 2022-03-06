# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExpresstribuneTechItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    excerpt = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    image = scrapy.Field()
    storyLocation = scrapy.Field()
    story = scrapy.Field()

    pass
