import scrapy

class QuotesSpider(scrapy.Spider):
    name = "Analise"
    
    #COLOCAR O @ DO TIKTOK AQUI
    pp = "@mizzy1337"
    
    start_urls = ["https://www.tiktok.com/"+pp]

    def parse(self, response):
        a = response.xpath(
            '*//div[@class="tiktok-x6y88p-DivItemContainerV2 e19c29qe7"]'
        )
        for q in a:
            yield {
                "view": q.xpath(".//strong[@data-e2e='video-views']/text()").getall()
            }