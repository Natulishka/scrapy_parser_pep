import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    '''Паук PEP.'''

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        '''Парсит ссылки не страницы pep.'''
        for pep_link in response.css('#numerical-index td a::attr(href)'
                                     ).getall():
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        '''Парсит информацию со страницы pep.'''
        text_match = re.search(r'PEP (\d+) – ([\w ]+)', response.css(
            'h1.page-title::text').get())
        number, name = text_match.groups()
        data = {
            'number': number,
            'name': name,
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
