from typing import Generator

import scrapy
from scrapy.http import Response


class TechnologiesSpider(scrapy.Spider):
    name = "technologies"
    allowed_domains = ["www.work.ua"]
    start_urls = ["https://www.work.ua/jobs-python+developer/"]

    def parse(self, response: Response, **kwargs) -> Generator:
        job_vacancies = response.css(".cut-top.cut-bottom a::attr(href)").getall()
        for vacancy in job_vacancies:
            yield scrapy.Request(
                url=response.urljoin(vacancy), callback=self._parse_single_book
            )

        next_page = response.css(
            "#pjax-job-list > nav > "
            "ul.pagination.text-center.hidden-xs > "
            "li.no-style.add-left-default > a::attr(href)"
        ).get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def _parse_single_book(self, response: Response) -> Generator:
        technologies = response.css(
            ".flex.flex-wrap.w-100.toggle-block."
            "overflow.block-relative.js-toggle-block > "
            "span > span::text"
        ).getall()
        yield {
            "technologies": technologies,
        }
