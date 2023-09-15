import scrapy
from ..items import Proyectoscrapy1Item



class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls=['https://quotes.toscrape.com/']


    def parse(self, response):
        items = Proyectoscrapy1Item()
        div=response.css('.quote')
        for i in div:
            text = i.css(".text::text").getall()  ## response.css(".text::text").getall()scrapt
            autor = i.css(".author::text").getall()

            items['autor']=autor
            items['texto']= text

            yield items

        ## Correr con scrapy crawl quotes
        ## En caso salga error win32 api, instalar
        ## scrapy shell "https://quotes.toscrape.com/"
        ## response.xpath("//span[@class='text']/text()").getall()
        ## response.xpath("//span[@class='text']/text()").getall()[0]
        ## response.xpath("//span[@class='text']/text()").extract()
        ## response.xpath("//span[@class='text']/text()")[0].extract()
        ## Guardar el output en json: scrapy crawl quotes -o items.json
        ## Guardar el output en csv: scrapy crawl quotes -o items.csv
        ## Guardar el output en xlm: scrapy crawl quotes -o items.xml
        ## 'json', 'jsonlines', 'jsonl', 'jl', 'csv', 'xml', 'marshal', 'pickle'


"""    def parse(self, response):
        div=response.css('.quote')
        for i in div:
            text = i.css(".text::text").getall()  ## response.css(".text::text").getall()scrapt
            autor = i.css(".author::text").getall()
            yield {'Texto': text,
                    'Autor': autor
               }
"""