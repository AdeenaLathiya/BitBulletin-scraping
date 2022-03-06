import scrapy
from ..items import ExpresstribuneTechItem

class ExpresstribuneTechSpider(scrapy.Spider):
    name = 'expressTribune_tech'
    start_urls = ['https://tribune.com.pk/Technology?page=1']

    def parse(self,response):
        for all_news_link in response.css('ul.listing-page li div.row div.col-md-8 div.horiz-news3-caption a::attr(href)'):
            yield response.follow(all_news_link.get(), callback=self.parse_news)


    def parse_news(self, response):
        items = ExpresstribuneTechItem()
        
        all_news = response.css('div.storypage')

        for news in all_news:
            
          title = news.css('div.story-box-section h1::text').get()
          excerpt = news.css('div.story-box-section p.story-excerpt::text').get()
          author = news.css('div.story-box-section span.storypage-leftside div.left-authorbox span a::text').get()
          date = news.css('div.story-box-section span.storypage-leftside div.left-authorbox span::text')[1].get()
          image = news.css('div.story-box-section div.mainstorycontent-parent div.storypage-main-section2 div.storypage-rightside span.top-big-img div.story-featuredimage div.amp-top-main-img div.featured-image-global img::attr(src)').get()
          storyLocation = news.css('div.story-box-section div.mainstorycontent-parent div.storypage-main-section2 div.storypage-rightside span.story-text strong.location-names::text').get().strip()
          story = news.css('div.story-box-section div.mainstorycontent-parent div.storypage-main-section2 div.storypage-rightside span.story-text p::text').getall()


          items['title'] = title
          items['excerpt'] = excerpt
          items['author'] = author
          items['date'] = date
          items['image'] = image
          items['storyLocation'] = storyLocation
          items['story'] = story

          yield items
