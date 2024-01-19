import scrapy


class UsptoDatabaseSpider(scrapy.Spider):
    name = "uspto_database"
    allowed_domains = ["www.uspto.gov"]
    start_urls = ["https://www.uspto.gov"]

    def parse(self, response):
        pass
