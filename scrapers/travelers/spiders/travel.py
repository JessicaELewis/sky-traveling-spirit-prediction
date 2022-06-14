import scrapy


class TravelerSpider(scrapy.Spider):
    name = "travelers"

    def start_requests(self):
        urls = [
            'https://sky-children-of-the-light.fandom.com/wiki/Traveling_Spirits',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        table = response.css("table.article-table.sortable").extract_first()
        rows = table.xpath('//tr')

        for row in rows:
            yield {
                'visit': row.xpath('td[1] small//text()').extract_first(),
                'date': row.xpath('td[2] small//text()').extract_first(),
                'season': row.xpath('td[3] small//text()').extract_first(),
                'realms': row.xpath('td[4] small//text()').extract_first(),
                'spirit': row.xpath('td[5] small//text()').extract_first(),
                'lastvisit': row.xpath('td[6] small//text()').extract_first(),
            }
           

            # yield {
            #     'spirits': spirit
            # }

        # result = {}
        # headers = response.xpath('//table[@class="article-table"]/thead/th[1]/th[position() > 1]/text()').getall()
        # for row in response.xpath('//table[@class="article-table"]/tbody/tr[position() > 1][position() < last()]'):
        #     # field_name = row.xpath('./th/text()').get()
        #     values = row.xpath('./td/text()').getall()
        #     for header, value in zip(headers, values):
        #         result[f'{header}'] = value



        # filename = f'traveling_spirits.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
