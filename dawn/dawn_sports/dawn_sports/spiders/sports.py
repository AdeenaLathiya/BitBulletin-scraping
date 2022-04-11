import scrapy
from ..items import DawnSportsItem, DawnTechItem
class DawnSportsSpider(scrapy.Spider):
    name = 'newsSports'
    # start_urls = []

    def start_requests(self):
        yield scrapy.Request('https://www.dawn.com/sport',callback=self.parse1)
        yield scrapy.Request('https://www.dawn.com/tech',callback=self.parse2)
    
    def parse1(self, response):
        for newsLink in response.css("h2.story__title a::attr(href)"):
            yield response.follow(newsLink.get(), callback=self.parse_news)

    def parse_news(self, response):
        items = DawnSportsItem()

        title = response.css("h2.story__title a.story__link::text").extract_first().strip() ,
        author = response.css("span.story__byline a.story__byline__link::text").extract_first() ,
        article = response.css("p::text").extract(),
        picture = response.css("figure.media--uneven div.media__item  picture img::attr(src)").extract(),
        time = response.css("span.story__time span.timestamp--time span.timestamp__time::text").extract(), 
        date = response.css("span.story__time span.timestamp--date::text").extract() 
        category = 'Sports'

        items['title'] = title
        items['author'] = author
        items['article'] = article
        items['picture'] = picture
        items['time'] = time
        items['date'] = date
        items['category'] = category

        yield items

    def parse2(self, response):
        for newsLink in response.css("h2.story__title a::attr(href)"):
            yield response.follow(newsLink.get(), callback=self.parse_news2)

    def parse_news2(self, response):
        items2 = DawnTechItem()

        title2 = response.css("h2.story__title a.story__link::text").extract_first().strip() ,
        author2 = response.css("span.story__byline a.story__byline__link::text").extract_first() ,
        article2 = response.css("p::text").extract(),
        picture2 = response.css("figure.media--uneven div.media__item  picture img::attr(src)").extract(),
        # time = response.css("span.story__time span.timestamp--time span.timestamp__time::text").extract(), 
        date2 = response.css("span.story__time span.timestamp--date::text").extract() 
        category2 = 'Tech' 

        items2['title2'] = title2
        items2['author2'] = author2
        items2['article2'] = article2
        items2['picture2'] = picture2
        # items['time'] = time
        items2['date2'] = date2
        items2['category2'] = category2

        yield items2