# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontestItem


class AmazontestspiderSpider(scrapy.Spider):
    name = 'amazontest'
    page_number = 2
    start_urls = [
        'https://www.amazon.com/s?k=computer+monitor&sprefix=compu%2Caps%2C451&ref=nb_sb_ss_pltr-ranker-1hour_2_5'
        ]

    def parse(self, response):
        items = AmazontestItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_price = response.css('.a-price-fraction , .widgetId\=search-results_4 .a-price-whole').css('::text').extract()
        
        items['product_name'] = product_name
        items['product_price'] = product_price

        yield items

        next_page = 'h ttps://www.amazon.com/s?k=computer+monitor&page=' + str(AmazontestspiderSpider.page_number) + '&qid=1667114794&sprefix=compu%2Caps%2C451&ref=sr_pg_2'
        if AmazontestspiderSpider.page_number <= 20:
            AmazontestspiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)