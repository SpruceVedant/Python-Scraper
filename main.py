# TEST ENUMERATION #
# Import libraries
import scrapy
from scrapy.crawler import CrawlerProcess
import pymongo

# Connect to MongoDB through mongo client 
client = pymongo.MongoClient("mongodb://localhost:27017/")#mongo url here 
db = client["leclerc_fr"]
collection = db["products"]

class LeclercSpider(scrapy.Spider):
    name = "leclerc_spider"
    start_urls = [
        'https://www.e.leclerc/cat/sport-loisirs',
        'https://www.e.leclerc/cat/vetements'
    ]
    
    def parse(self, response):
        products = response.css('.product-item')
        for product in products:
            product_name = product.css('.product-title::text').get()
            product_price = product.css('.price::text').get()
            product_image = product.css('.product-image img::attr(src)').get()
            
            product_data = {
                'name': product_name,
                'price': product_price,
                'image': product_image
            }
            collection.insert_one(product_data)

# Run the spider
if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(LeclercSpider)
    process.start()
