import scrapy
from ..items import DawnBusinessItem

class DawnBusinessSpider(scrapy.Spider):
    name = 'business'
    start_urls = ['https://www.dawn.com/business']

    def parse(self, response):
        for newsLink in response.css("h2.story__title a::attr(href)"):
            yield response.follow(newsLink.get(), callback=self.parse_news)

    def parse_news(self, response):
        items = DawnBusinessItem()

        title = response.css("h2.story__title a.story__link::text").extract_first().strip() ,
        author = response.css("span.story__byline a.story__byline__link::text").extract_first() ,
        article = response.css("p::text").extract(),
        picture = response.css("figure.media--uneven div.media__item  picture img::attr(src)").extract(),
        time = response.css("span.story__time span.timestamp--time span.timestamp__time::text").extract(), 
        date = response.css("span.story__time span.timestamp--date::text").extract()  

        items['title'] = title
        items['author'] = author
        items['article'] = article
        items['picture'] = picture
        items['time'] = time
        items['date'] = date

        yield items
