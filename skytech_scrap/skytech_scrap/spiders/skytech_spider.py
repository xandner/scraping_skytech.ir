import scrapy
from ..items import SkytechScrapItem


class SkythechDpider(scrapy.Spider):
    def __init__(self):
        self.crawled=set()
    name = 'skythech'
    start_urls = ['http://skytech.ir/']
    BASE_URL = 'http://skytech.ir/'

    def parse(self, response):

        if response.url == self.BASE_URL:

            all_tag_products = response.xpath("//ul[@id='sideManu']")
            for all_tag_product in all_tag_products:
                products = all_tag_product.xpath("//li[@class='subMenu']/ul/table")

                for product in products:
                    product_url = product.css('tr td li a::attr(href)').extract()
                    for url in product_url:
                        final_product_url = response.urljoin(url)
                        yield scrapy.Request(final_product_url, callback=self.parse)
        else:
            items = SkytechScrapItem()
            img = []

            pic = response.css('div.thumbnail a img::attr(src)').extract()
            name = response.css('div.caption h5 a font::text').extract()
            price = response.xpath(
                "//div[@class='caption']/h5/span[@class=re:test(@class,'ContentPlaceHolder*Pre_PRICELabel*')]/font/text()").extract()
            for image_url in pic:
                img.append(response.urljoin(image_url))
            items['name'] = name
            items['price'] = price
            items['number'] = price
            items['image'] = img
            yield items

            next_page=response.css('div span a::attr(href)').extract()
            if next_page is not None:
                for url in next_page:
                    final_product_url = response.urljoin(url)
                    if final_product_url not in self.crawled:
                        self.crawled.add(final_product_url)
                        yield scrapy.Request(final_product_url, callback=self.parse)


