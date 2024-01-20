import scrapy
import json

class UsptoBulkdataSpider(scrapy.Spider):
    name = "uspto_bulkdata"
    allowed_domains = ["developer.uspto.gov"]
    start_urls = ["https://developer.uspto.gov/ibd-api/v1/application/publications?inventionSubjectMatterCategory=utility&publicationFromDate=1994-02-08&publicationToDate=2020-02-08"]
    
    def start_requests(self):
        yield scrapy.Request(url='https://developer.uspto.gov/ibd-api/v1/application/publications?inventionSubjectMatterCategory=utility&publicationFromDate=1994-02-08&publicationToDate=2020-02-08', callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'})

    def parse(self, response):
        # yield response.follow(url='https://developer.uspto.gov/ibd-api/v1/application/publications?inventionSubjectMatterCategory=utility&publicationFromDate=1994-02-08&publicationToDate=2020-02-08', callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'})
        # print(response.body)
        
        json_response = json.loads(response.body)
        claimText = json_response.get('claimText')
        #print(claimText)

        #for claim in claimText:
            #yield {
                    #'claimText':claim.get('claimText')
                #}
        
