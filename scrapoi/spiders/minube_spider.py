import scrapy
from scrapoi.items import PoiItem
from string import Template

class MinubeSpider(scrapy.Spider):
    name = "minube"
    allowed_domains = ["minube.co.uk"]

    def __init__(self, country='spain', *args, **kwargs):
        """
        In the init method we retrieve the country parameter and initialize the html poi list
        as an empty string.
        """
        super(MinubeSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.minube.co.uk/what-to-see/%s' % country]
        self.poi_list = ''
        self.country_name = country

    def parse(self, response):
        """
        This method parses two kind of data from MiNube website: names and descriptions
        from points of interest in the website.
        """
        for sel in response.xpath("//li[contains(@class, 'poi_cont_desc')]"):
            item = PoiItem()
            item['name'] = sel.xpath('div/span/div/a/@title').extract()[0].encode('utf-8')
            item['desc'] = sel.xpath('div/div[contains(@class, "poi_descript")]/text()').extract()[0].encode('utf-8')
            self.poi_list += '<dt>%s</dt><dd>%s</dd>' % (item['name'], item['desc'])
            yield item

    def closed(self, reason):
        """
        This method is called when the crawling process is finished and it generates
        a html file based in a template with the parsed data.
        """
        if reason == 'finished':
            with open ("index_template.html", "r") as t:
                s = Template(t.read().replace('\n', ''))
            with open('index.html', 'w') as f:
                f.write(s.substitute(country=self.country_name, poi_list=self.poi_list))
