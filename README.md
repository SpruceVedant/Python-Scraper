# Python-Scraper
Set up a MongoDB connection and insert the extracted data into the database.
Test your spider by running scrapy crawl spidername.


Install Scrapy framework by running pip install scrapy
```
pip install scrapy
```


Create a new Scrapy project by running
```
scrapy startproject <projectname>
```

Create a new Scrapy spider by running
```
scrapy genspider <spidername>
```
Test your spider by running scrapy crawl spidername.
```
scrapy crawl <spidername>
```



Define the structure of the product data you want to scrape in the spider file using xpath selectors or css selectors.

In the settings.py file of your Scrapy project, you need to set the following:
Enable the ```ITEM_PIPELINES``` setting and add ```leclerc.pipelines.MongoDBPipeline``` to it. This setting tells Scrapy to use the MongoDB pipeline to process the scraped data.
Set the ```MONGO_URI``` and ```MONGO_DATABASE``` settings to the values you want to use for your MongoDB connection.
In the pipelines.py file of your Scrapy project, you need to paste the code for the MongoDB pipeline:


You will need to specify the MongoDB URL in the Scrapy settings file, which is usually named settings.py and located in your project directory.
```
# settings.py

# ...

# MongoDB settings
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = '<your_database_name>'

# ...
```

