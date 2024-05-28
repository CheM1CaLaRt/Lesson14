import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css('div._Ud0k')
        for light in lights:
            yield {
                'name': light.css('div.lsooF span::text').get(),
                'price': light.css('div.pY3d2 span::text').get(),
                'url': light.css('a').attrib['href']
            }

    def closed(self, reason):
        # Функция, вызываемая после завершения работы спайдера
        # Открываем файл для записи и записываем данные в него
        with open('lights.csv', mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['name', 'price', 'url']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in self.items():
                writer.writerow(item)