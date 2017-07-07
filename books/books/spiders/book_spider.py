from scrapy import Selector
from scrapy.spiders import CrawlSpider
from pyvirtualdisplay import Display

from ..items import BooksItem
from selenium import webdriver


class AboutRestSpider(CrawlSpider):
    name = "books"

    allowed_domains = ["adlibris.com"]

    start_urls = [
        'http://www.adlibris.com/se/avdelning/bilderbocker-9510?id=9510&pn=0'
    ]

    def parse(self, response):
        no_data = '-'
        for each in response.selector.xpath('.//div[@class="section search results"]/ul').xpath('li'):
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
                item['isbn'] = each.xpath('.//div[@class="price-from"]/span').re_first(r'ISBN \d+')
            except:
                item['isbn'] = no_data
            try:
                item['age_range'] = each.xpath('.//span[@itemprop="typicalAgeRange"]/text()').extract_first()
            except:
                item['age_range'] = no_data
            try:
                item['book_format'] = each.xpath('.//span[@class="book-format"]/text()').extract_first()
            except:
                item['book_format'] = no_data
            try:
                current_price = each.xpath('.//div[@class="current-price"]/text()').extract_first()
                currency = each.xpath('.//span[@class="currency"]/text()').extract_first()
                item['current_price'] = '%s%s' % (current_price, currency)
            except:
                item['current_price'] = no_data
            try:
                item['image'] = each.xpath('.//div[@class="img"]/a/img/@data-original').extract_first()
            except:
                item['image'] = no_data
            yield item

    # def __init__(self, *a, **kw):
    #     super().__init__(*a, **kw)
    #     self.display = Display(visible=0, size=(1024, 768))
    #     self.display.start()
    #     self.driver = webdriver.Firefox()

    # def parse(self, response):
    #     self.driver.get(response.url)
    #     while True:
    #         try:
    #             next = self.driver.find_element_by_xpath(
    #                 './/div[@class="ui_column is-3 language"]/ul/li/span[@class="toggle"]/input[@id="taplc_location_review_filter_controls_0_filterLang_ALL"]')
    #             next.click()
    #             selenium_response_text = self.driver.page_source
    #             new_selector = Selector(text=selenium_response_text)
    #             for each in new_selector.xpath('//div[@id="PAGE"]'):
    #                     item['']
    #                 yield item
    #         except:
    #             break
    #     self.driver.close()
    #     self.display.stop()
