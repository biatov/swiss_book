# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from datetime import datetime


class BooksPipeline(object):
    def __init__(self):
        self.date = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        self.file = csv.writer(open('books_%s.csv' % self.date, 'w'), quoting=csv.QUOTE_MINIMAL)
        self.file.writerow(
            ['Title', 'Author', 'Published Year', 'ISBN', 'Age Range', 'Book Format', 'Current Price', 'Image']
        )

    def process_item(self, item, spider):
        self.file.writerow([item['title'], item['author'], item['published_year'], item['isbn'], item['age_range'],
                            item['book_format'], item['current_price'], item['image']])
        return item
