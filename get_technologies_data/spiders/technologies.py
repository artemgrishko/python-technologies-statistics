import scrapy


class TechnologiesSpider(scrapy.Spider):
    name = "technologies"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python"]

    def parse(self, response):
        pass
