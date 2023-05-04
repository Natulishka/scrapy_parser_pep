import scrapy


class PepParseItem(scrapy.Item):
    '''Items для PEP.'''

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
