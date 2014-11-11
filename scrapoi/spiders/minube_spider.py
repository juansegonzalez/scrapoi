import scrapy
from scrapoi.items import PoiItem

class MinubeSpider(scrapy.Spider):
    name = "minube"
    allowed_domains = ["minube.co.uk"]
    start_urls = [
        "http://www.minube.co.uk/what-to-see/italy"
    ]

    def parse(self, response):
        for sel in response.xpath("//li[contains(@class, 'poi_cont_desc')]"):
            item = PoiItem()
            item['name'] = sel.xpath('div/span/div/a/@title').extract()
            item['link'] = sel.xpath('div/span/div/a/@href').extract()
            item['desc'] = sel.xpath('div/div[contains(@class, "poi_descript")]/text()').extract()
            yield item
