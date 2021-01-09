# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SkytechScrapItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # number = scrapy.Field()
    price = scrapy.Field()
    number = scrapy.Field()
    # image=scrapy.Field()
