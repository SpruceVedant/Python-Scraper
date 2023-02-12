# Importing Required Libraries
import scrapy
import re
from pymongo import MongoClient

# Creating a MongoDB Client
client = MongoClient()
db = client["<yourname>"]
collection = db["leclerc_fr"]

# Defining the Spider Class
class LeclercFrSpider(scrapy.Spider):
    name = "leclerc_fr"
    start_urls = [
        'https://www.e.leclerc/cat/sport-loisirs',
        'https://www.e.leclerc/cat/vetements'
    ]
    
    # Define the Parsing Function
    def parse(self, response):
        product_category = response.url.split("/")[-1]
        for product in response.css("div.product-item"):
            product_data = {
                "name": product.css("a.product-title::text").get(),
                "brand": product.css("div.brand::text").get(),
                "original_price": float(product.css("span.price-regular::text").get().strip("€").replace(",", ".")),
                "sale_price": float(product.css("span.price-discount::text").get().strip("€").replace(",", ".")),
                "image_url": product.css("img.lazyload::attr(src)").get(),
                "product_page_url": response.urljoin(product.css("a.product-title::attr(href)").get()),
                "product_category": product_category,
                "stock": bool(product.css("div.product-outofstock::text").get()),
                "sku": product.css("a.product-title::attr(href)").get().split("/")[-1].split("-")[0],
                "ean": product.css("div.product-gtin13::text").get()
            }
            collection.insert_one(product_data)

# Run the Spider
if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess(settings={
        "FEED_FORMAT": "json",
        "FEED_URI": "output.json"
    })

    process.crawl(LeclercFrSpider)
    process.start()
