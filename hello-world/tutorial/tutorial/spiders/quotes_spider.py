import scrapy
from scrapy.http.response.html import HtmlResponse

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response:HtmlResponse):
        titulo = response.xpath('//h1/a/text').get()
        citas = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        with open('resultados.html', 'w', encoding='utf-8') as f:
            f.write(response.text)