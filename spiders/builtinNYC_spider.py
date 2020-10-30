from scrapy import Spider, Request
from builtinNYC.items import BuiltinnycItem
import re

class BuiltinNYCSpider(Spider):
    name = 'builtinNYC_spider'
    start_urls = ['https://www.builtinnyc.com/companies?status=all&page=1']
    allowed_urls = ['https://www.builtinnyc.com/']

    # for url in start_urls:
    #     yield Request(url=url, callback=self.parse)

    def parse(self, response):

        url_list = [f'https://www.builtinnyc.com/companies?status=all&page={i+201}'
                    for i in range(70)]

        for url in url_list:
            
            yield Request(url=url, callback=self.parse_result_page)

    def parse_result_page(self, response):

        try:
            comp_url_all = response.xpath('//div[@class="wrap-view-page"]/a/@href').extract()
        except:
            print('*****No Company URL List!!!*****')
            print(f'Offending URL: {response.url}')
            comp_url_all = [None]*20

        num = len(comp_url_all)

        try:
            company_all = response.xpath('//div[@class="main-content-first"]/div[@class="title"]/span/text()').extract()
        except:
            print('*****No Company List!!!*****')
            print(f'Offending URL: {response.url}')
            company_all = [None]*num      

        try: 
            jobs_all = response.xpath('//div[@class="right_column"]/div[@class="open-jobs"]/span/a/text()').extract()
        except:
            print('*****No Jobs List!!!*****')
            print(f'Offending URL: {response.url}')
            jobs_all = [None]*num

        for i in range(num):

            try:
                company = company_all[i]
            except:
                company = None

            try: 
                jobs = jobs_all[i]
            except:
                jobs= None  

        # try:
        #     description_all = response.xpath('//div[@class="main-content-first"]/div[@class="company-description"]/span/text()').extract()
        # except:
        #     print('*****No Description List!!!*****')
        #     print(f'Offending URL: {response.url}')
        #     description_all = [None]*num

        # try:
        #     job_type_all = response.xpath('//div[@class="main-content-first"]/div[@class="company-type"]/span/text()').extract()
        # except:
        #     print('*****No Job Type List!!!*****')
        #     print(f'Offending URL: {response.url}')
        #     job_type_all = [None]*num          

        # try:
        #     address_all = response.xpath('//div[@class="company-address"]/div[@class="address-field"]/text()').extract()
        # except:
        #     print('*****No Address List!!!*****')
        #     print(f'Offending URL: {response.url}')
        #     address_all = [None]*num

            # try:
            #     description = description_all[i]
            # except:
            #     description = None

            # try:
            #     job_type = job_type_all[i]
            # except:
            #     job_type = None


            # try:
            #     address = address_all[i]
            # except:
            #     address = None

            # meta = {'company': company, 'description': description,
            #         'job_type': job_type, 'jobs': jobs, 'address': address}

            meta = {'company': company,'jobs': jobs}

            comp_url = 'https://www.builtinnyc.com' + comp_url_all[i]

            yield Request(url=comp_url, callback=self.parse_comp_page, meta=meta)

    def parse_comp_page(self, response):

        try:
            i_name = response.xpath('//div[@class="company-card-title"]/div[@class="title-row"]/h1/text()').extract()
        except:
            print('*****No Name available!!!*****')
            print(f'Offending URL: {response.url}')
            date = None

        try:
            date = response.xpath('//div[@class="company-card-title"]/div/div[@class="item item-founded"]/time[@class="datetime"]/text()').extract()
        except:
            print('*****No Date available!!!*****')
            print(f'Offending URL: {response.url}')
            date = None

        try:
            job_type = response.xpath('//div[@class="col col-industry"]/div[@class="item"]/text()').extract()
        except:
            print('*****No Job Type available!!!*****')
            print(f'Offending URL: {response.url}')
            funding = None

        try:
            funding = response.xpath('//div[@class="col-sub field_year_founded"]/div[@class="item"]/text()').extract()
        except:
            print('*****No Funding available!!!*****')
            print(f'Offending URL: {response.url}')
            funding = None
            
        try:
            loc_employ = response.xpath('//div[@class="col-sub field_local_employees"]/div[@class="item"]/text()').extract()
        except:
            print('*****No Local Employees available!!!*****')
            print(f'Offending URL: {response.url}')
            loc_employ = None
            
        try:
            tot_employ = response.xpath('//div[@class="col-sub field_total_employees"]/div[@class="item"]/text()').extract()
        except:
            print('*****No Total Employees available!!!*****')
            print(f'Offending URL: {response.url}')
            tot_employ = None 
        
        try:
            description = response.xpath('//div[@class="company-overview-content"]/div[@class="row first-child"]/div[@class="col-2"]/div[@class="description"]/text()').extract()
        except:
            print('*****No Description available!!!*****')
            print(f'Offending URL: {response.url}')
            tot_employ = None

        try:
            address = response.xpath('//div[@class="gmap_location_widget_description company_description"]/text()').extract()
        except:
            print('*****No Address available!!!*****')
            print(f'Offending URL: {response.url}')
            tot_employ = None                 

        # try:
        #      location = response.xpath('//div[@class="company-card-title"]/div/div[@class="item item-locality"]/text()').extract()
 
        # except:
        #     print('*****No Location available!!!*****')
        #     print(f'Offending URL: {response.url}')
        #     location = None

        

        item = BuiltinnycItem()
        item['i_name'] = i_name
        item['date'] = date
        item['job_type'] = job_type
        item['funding'] = funding
        item['loc_employ'] = loc_employ
        item['tot_employ'] = tot_employ
        item['description'] = description
        item['address'] = address
        item['company'] = response.meta['company']
        item['jobs'] = response.meta['jobs']
        # item['location'] = location
        # item['description'] = response.meta['description']
        # item['job_type'] = response.meta['job_type']
        # item['address'] = response.meta['address']

        yield item







