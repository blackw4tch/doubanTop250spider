from scrapy import Request
from scrapy.spiders import Spider
from doubantop250.items import Doubantop250Item
class doubanTop250Spider(Spider):
    name = "movie"
    allowed_domains = ["movie.douban.com"]
    page = 0

    def start_requests(self):
        url = "https://movie.douban.com/top250?start=0"
        yield Request(url,callback = self.douban_parse)

    def douban_parse(self,response):

        item = Doubantop250Item()
        list_selector = response.xpath("//div[@class='item']")
        for one_selector in list_selector:
            title = one_selector.xpath("div[2]/div[1]/a/span[1]/text()").extract()[0]
            cast = one_selector.xpath("div[2]/div[2]/p[1]/text()[1]").extract()[0]
            rate = one_selector.xpath("div[2]/div[2]/div/span[2]/text()").extract()[0]
            quote = one_selector.xpath("div[2]/div[2]/p[2]/span/text()").extract()[0]
            number = one_selector.xpath("div[2]/div[2]/div/span[4]/text()").extract()[0]
            image_url = one_selector.xpath("div[1]/a/img/@src").extract()[0]
            item["title"] = title
            item["cast"] = cast
            item["rate"] = rate
            item["quote"] = quote
            item["number"] = number
            item["image_urls"] = [image_url]
            yield item

        if self.page <= 225:
            self.page += 25
            next_url = "https://movie.douban.com/top250?start=%d"%(self.page)
            yield Request(next_url,callback=self.douban_parse)