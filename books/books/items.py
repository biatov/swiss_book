# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    published_year = scrapy.Field()
    isbn = scrapy.Field()
    age_range = scrapy.Field()
    book_format = scrapy.Field()
    current_price = scrapy.Field()
    image = scrapy.Field()
