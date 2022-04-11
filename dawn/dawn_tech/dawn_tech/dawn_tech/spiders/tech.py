import scrapy
from ..items import DawnTechItem

class DawnTechSpider(scrapy.Spider):
    name = 'newsTech'
    start_urls = ['https://www.dawn.com/tech']

    def parse(self, response):
        for newsLink in response.css("h2.story__title a::attr(href)"):
            yield response.follow(newsLink.get(), callback=self.parse_news)

    def parse_news2(self, response):
        items2 = DawnTechItem()

        title2 = response.css("h2.story__title a.story__link::text").extract_first().strip() ,
        author2 = response.css("span.story__byline a.story__byline__link::text").extract_first() ,
        article2 = response.css("p::text").extract(),
        picture2 = response.css("figure.media--uneven div.media__item  picture img::attr(src)").extract(),
        # time = response.css("span.story__time span.timestamp--time span.timestamp__time::text").extract(), 
        date2 = response.css("span.story__time span.timestamp--date::text").extract()  

        items2['title2'] = title2
        items2['author2'] = author2
        items2['article2'] = article2
        items2['picture2'] = picture2
        # items['time'] = time
        items2['date2'] = date2

        yield items2
