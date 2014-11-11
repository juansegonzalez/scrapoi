import scrapy
from scrapoi.items import PoiItem
from string import Template

class MinubeSpider(scrapy.Spider):
    name = "minube"
    allowed_domains = ["minube.co.uk"]

    def __init__(self, country='spain', *args, **kwargs):
        super(MinubeSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.minube.co.uk/what-to-see/%s' % country]
        self.poi_list = ''
        self.country_name = country

    def parse(self, response):
        for sel in response.xpath("//li[contains(@class, 'poi_cont_desc')]"):
            item = PoiItem()
            item['name'] = sel.xpath('div/span/div/a/@title').extract()[0].encode('utf-8')
            item['link'] = sel.xpath('div/span/div/a/@href').extract()[0].encode('utf-8')
            item['desc'] = sel.xpath('div/div[contains(@class, "poi_descript")]/text()').extract()[0].encode('utf-8')
            self.poi_list += '<li><a title="%s" href="%s">%s</a><p>%s</p></li>' % (item['name'], item['link'], item['name'], item['desc'])
            yield item

    def closed(self, reason):
        if reason == 'finished':
            with open ("index_template.html", "r") as t:
                s = Template(t.read().replace('\n', ''))
            with open('index.html', 'w') as f:
                f.write(s.substitute(country=self.country_name, poi_list=self.poi_list))
