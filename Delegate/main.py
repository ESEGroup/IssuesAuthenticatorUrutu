import requests
import scrapy
from scrapy.crawler import CrawlerProcess


class ConnectedMacs(scrapy.Item):
    devices = scrapy.Field()


# Proof of Concept:
# This was done on a (passwordless) D-link DIR-809 home router.
# We still need to study the model on the actual labs
class RouterSpider(scrapy.Spider):
    name = 'router_spider'
    start_urls = ['http://192.168.0.1/Status/wifi_assoc.asp']

    def parse(self, response):
        # Get macs
        macs = response.xpath('//mac/text()').extract()
        # print(macs)

        # Send connected macs to server
        # TODO  get issues monitoring endpoint
        url = 'http://localhost/counter.php'
        payload = {'macs[]': macs}
        r = requests.post(url, data=payload)
        # print(r.text)

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'LOG_ENABLED': False
})

process.crawl(RouterSpider)
process.start()
