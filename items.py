# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BuiltinnycItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()
    i_name = scrapy.Field()
    job_type = scrapy.Field()
    address = scrapy.Field()
    date = scrapy.Field()
    funding = scrapy.Field()
    jobs = scrapy.Field()
    loc_employ = scrapy.Field()
    tot_employ = scrapy.Field()
    description = scrapy.Field()
    