import scrapy
from table import Table

class TravelerSpider(scrapy.Spider):
    name = "travelers"

    def start_requests(self):
        urls = [
            'https://sky-children-of-the-light.fandom.com/wiki/Traveling_Spirits',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        respath = '//child::table[contains(concat(" ", normalize-space(@class), " "), " article-table ")][1]'

        print(response.xpath(respath))

        table = Table(response.xpath(respath))
        # yield all rows
        yield from table.as_dicts()

        # table = response.css("table.article-table tr").extract()
        # # rows = table.xpath('tr')

        # for row in table:
        #     yield {
        #         'visit': row.xpath('td[1]').extract_first(),
        #         'date': row.xpath('td[2]').extract_first(),
        #         'season': row.xpath('td[3]').extract_first(),
        #         'realms': row.xpath('td[4]').extract_first(),
        #         'spirit': row.xpath('td[5]').extract_first(),
        #         'lastvisit': row.xpath('td[6]').extract_first(),
        #     }

        # print(self.crawler.stats.set_value())