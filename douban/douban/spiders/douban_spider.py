from scrapy.contrib.spiders import CrawlSpider

class Douban(CrawlSpider):
    name = "doubanTest"
    start_urls = "http://movie.douban.com/top250"

    def parse(self,response):
        print response.body