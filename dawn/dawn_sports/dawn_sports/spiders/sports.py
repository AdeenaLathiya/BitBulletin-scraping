import scrapy
from ..items import DawnSportsItem, DawnTechItem

class DawnSportsSpider(scrapy.Spider):
    name = 'newsSports'
    # start_urls = []
    start_urls = ['https://www.dawn.com/sport']

    # def __init__(self):
    #     self.start_urls = []

    def parse(self, response):
        for newsLink in response.css("h2.story__title a::attr(href)"):
            yield response.follow(newsLink.get(), callback=self.parse_news)

    # url = 'https://www.dawn.com/sport'
    # start_urls.append(url)

    def parse_news(self, response):
        items = DawnSportsItem()

        # url = 'https://www.dawn.com/sport'
        # start_urls.append(url)

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

        # start_urls.remove()

        # next_url = ['https://www.dawn.com/tech']
        # yield response.follow (next_url, callback=self.parse_news2)

    # start_urls = ['https://www.dawn.com/tech']    

    def parse(self, response):
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

        items2['title2'] = title2
        items2['author2'] = author2
        items2['article2'] = article2
        items2['picture2'] = picture2
        # items['time'] = time
        items2['date2'] = date2

        yield items2
    
