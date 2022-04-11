import scrapy
# from scrapy.http.request import Request
from ..items import DawnSportsItem, DawnTechItem
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.linkextractors import LinkExtractor

class DawnSportsSpider(scrapy.Spider):
    name = 'newsSports'
    start_urls = ['https://www.dawn.com/sport', 'https://www.dawn.com/tech']

    def parse_state(self, response):
        extractor = LinkExtractor(allow=r'%s+p\d+' % self.start_urls[0])

        for link in extractor.extract_links(response):
            if link == 'https://www.dawn.com/sport':
                print('link', link)
                yield scrapy.Request(link.url, callback=self.parse1)
            elif link == 'https://www.dawn.com/tech':
                yield scrapy.Request(link.url, callback=self.parse2)   

    def parse(self, response):
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

# settings = get_project_settings()
# process = CrawlerProcess(settings)
# process.crawl(DawnSportsSpider)
# process.crawl(DawnTechSpider)
# process.start() # the script will block here until all crawling jobs are finished