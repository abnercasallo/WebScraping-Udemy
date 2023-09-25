import  scrapy
from ..items import MercadoItem

class mercadoSpider(scrapy.Spider):
    name='mercado'
    page_number=51
    start_urls=['https://listado.mercadolibre.com.pe/computacion/laptops-accesorios/laptops/laptops_Desde_51_NoIndex_True']

    def parse(self, response):
        items= MercadoItem()

        description= response.css('.shops__item-title::text').getall()
        price= response.css('.ui-search-price__part--medium .andes-money-amount__fraction::text').getall()

        items['description']=description
        items['price']=price

        yield items
        next_page='https://listado.mercadolibre.com.pe/computacion/laptops-accesorios/laptops/laptops_Desde_'+str(mercadoSpider.page_number)+'_NoIndex_True'
        #'https://listado.mercadolibre.com.pe/computacion/laptops-accesorios/laptops/laptops_Desde_'+str(mercadoSpider.page_number)+'_NoIndex_True'

        if mercadoSpider.page_number<=2001:
            mercadoSpider.page_number+=50
            yield response.follow(next_page, callback=self.parse)


