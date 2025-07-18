import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.http import Response


class CameraSpider(scrapy.Spider):
    name = "Camera"
    allowed_domains = ["amazon.com"]

    def start_requests(self):
        url = (
            "https://www.amazon.com/s?k=RV+Backup+Camera+Wireless+Plug+and+Play&"
            "crid=1ZBZX33NJN3KU&sprefix=rv+backup+camera+wireless+plug+and+play%2Caps%2C738&ref=nb_sb_noss_1"
        )
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response: Response):
        products = response.xpath('//div[@data-component-type="s-search-result"]')
        for product in products:
            # ❌ Skip sponsored
            if product.xpath('.//span[@aria-label="Sponsored"]'):
                continue

            # ✅ Extract data
            title = product.xpath('.//h2/@aria-label').get() or product.xpath('.//h2/span/text()').get()
            rating = product.xpath('.//span[@class="a-icon-alt"]/text()').get()
            views = product.xpath('.//span[@class="a-size-base s-underline-text"]/text()').get()
            link = response.urljoin(product.xpath('.//a[@class="a-link-normal s-no-outline"]/@href').get())
            image = product.xpath('.//img[@class="s-image"]/@src').get()
            price_whole = product.xpath('.//span[@class="a-price-whole"]/text()').get()
            price_fraction = product.xpath('.//span[@class="a-price-fraction"]/text()').get()
            price = f"${price_whole}.{price_fraction}" if price_whole and price_fraction else None

            yield {
                'title': title,
                'rating': rating,
                'views': views,
                'link': link,
                'image': image,
                'price': price,
            }

        # 🔁 Handle pagination
        next_page = response.xpath('//a[contains(@class, "s-pagination-next")]/@href').get()
        if next_page:
            yield SeleniumRequest(url=response.urljoin(next_page), callback=self.parse)
