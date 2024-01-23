# probability density functions for time periods of relative tech content dependent upon year of innovation 
# implies more results given one time period = need more spiders for more precision acting in parallel
# where each spider needs its own User-Agent : contribution from Kelly Christiansen

import scrapy
import json

import pandas as pd
import datetime

class UsptoBulkdataSpider(scrapy.Spider):
    name = "uspto_bulkdata"
    allowed_domains = ["developer.uspto.gov"]
    start_urls = ["https://developer.uspto.gov/ibd-api/v1/application/publications?inventionSubjectMatterCategory=utility&publicationFromDate=1994-02-08&publicationToDate=2020-02-08"]
    
    def start_requests(self):
        # initializing dates
        fromDate = datetime.datetime(1994, 2, 8)
        toDate = datetime.datetime(2020, 2, 8)
        
        # initializing the number of spiders to process the time interval
        time_interval = 50
        
        # calculating time_interval_duration per number of spiders
        time_duration = toDate - fromDate
        time_frequency = time_duration // time_interval
        
        # use the pandas library to populate a range of dates
        dateRange = pd.date_range(start=fromDate, end=toDate, freq=time_frequency)
        
        # convert pandas calculation to desired format
        desiredTimeFormat = dateRange.strftime("%Y-%m-%d").tolist()
        print("N equal duration dates : " + str(desiredTimeFormat))
        print("The data type of the pandas object is : " + str(type(desiredTimeFormat)))
        print("The number of elements in the formatted-time list is : ", len(desiredTimeFormat))
        
        # loop through time intervals
        i = 0
        while i < len(desiredTimeFormat):
            time0 = desiredTimeFormat[i]
            i = i + 1
            time1 = desiredTimeFormat[i]
            
            # insert time interval elements into url scrapy request
            url0 = f"https://developer.uspto.gov/ibd-api/v1/application/publications?inventionSubjectMatterCategory=utility&publicationFromDate={time0}"
            url1 = "&"
            url2 = f"publicationToDate={time1}"
            
            # concatenate url string
            url3 = url0 + url1 + url2
            
            yield scrapy.Request(url= url3, callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'})
        
        #yield scrapy.Request(url= 'https://developer.uspto.gov/ibd-api/v1/application/publications?inventionSubjectMatterCategory=utility&publicationFromDate=1994-02-08&publicationToDate=2020-02-08', callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'})

    def parse(self, response):
        # yield response.follow(url='https://developer.uspto.gov/ibd-api/v1/application/publications?inventionSubjectMatterCategory=utility&publicationFromDate=1994-02-08&publicationToDate=2020-02-08', callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'})
        # print(response.body)
        
        json_response = json.loads(response.body)
        results = json_response.get('results')
        
        for result in results:
            yield {
                    'abstractText': result.get('abstractText')
                }
        
