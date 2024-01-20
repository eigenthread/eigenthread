import scrapy


class UsptoBulkdataSpider(scrapy.Spider):
    name = "uspto_bulkdata"
    allowed_domains = ["www.uspto.gov"]
    #start_urls = ["https://www.uspto.gov"]
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.uspto.gov', callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'})

    def parse(self, response):
        yield response.follow(url='https://www.uspto.gov', callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'})
