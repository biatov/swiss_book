from scrapy import Selector
from ..items import BooksItem
import scrapy


class AboutRestSpider(scrapy.Spider):
    name = "books"

    allowed_domains = ["adlibris.com"]

    start_urls = ['http://www.adlibris.com/se/avdelning/bilderbocker-9510?id=9510&pn=1']

    def parse(self, response):
        no_data = '-'
        next_page = response.xpath('.//a[@class="btn btn--show-more-large next"]/@href').extract_first()
        root = Selector(response)

        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        for each in root.xpath('.//div[@class="section search results"]/ul').xpath('li'):
            item = BooksItem()
            try:
                item['title'] = each.xpath('.//h3/text()').extract_first().strip()
            except:
                item['title'] = no_data
            try:
                item['author'] = each.xpath('.//h4/a/text()').extract_first().strip()
            except:
                item['author'] = no_data
            try:
                item['published_year'] = each.xpath('.//div[@class="price-from"]/span').xpath('text()').re_first(r'\d{4},').replace(',', '')
            except:
                item['published_year'] = no_data
            try:
                item['isbn'] = each.xpath('.//div[@class="price-from"]/span').re_first(r'ISBN \d+').split()[1]
            except:
                item['isbn'] = no_data
            try:
                age_range = each.xpath('.//span[@itemprop="typicalAgeRange"]/text()').extract_first()
                item['age_range'] = age_range if age_range else no_data
            except:
                item['age_range'] = no_data
            try:
                item['book_format'] = each.xpath('.//span[@class="book-format"]/text()').extract_first()
            except:
                item['book_format'] = no_data
            try:
                current_price = each.xpath('.//div[@class="current-price"]/text()').extract_first()
            except:
                current_price = no_data
            try:
                currency = each.xpath('.//span[@class="currency"]/text()').extract_first()
            except:
                currency = ''
            try:
                item['current_price'] = '%s%s' % (current_price, currency)
            except:
                item['current_price'] = no_data
            try:
                item['image'] = each.xpath('.//div[@class="img"]/a/img/@data-original').extract_first()
            except:
                item['image'] = no_data
            yield item

