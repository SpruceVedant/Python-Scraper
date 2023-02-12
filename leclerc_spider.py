import scrapy


class LeclercSpiderSpider(scrapy.Spider):
    name = "leclerc_spider"
    allowed_domains = ["www.e.leclerc"]
    start_urls = ["http://www.e.leclerc/"]

    def parse(self, response):
        pass
