import scrapy
from smzdm.items import SmzdmPhoneItem


class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['smzdm.com']
    start_urls = [f'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/']

    def parse(self, response):
        select = scrapy.Selector(response=response)
        #最多10个
        #position()<11未起作用[position()<11]
        for commentpage in select.xpath(
                '//div[@class="z-feed-foot-l"]/a[last()]/@href')[:10]:
            yield scrapy.Request(url=commentpage.extract(),
                                 callback=self.parse_comments)

    def parse_comments(self, response):
        select = scrapy.Selector(response=response)
        pages = select.xpath(
            '//div[@class="tab_info" and @id="commentTabBlockNew"]/ul[@class="pagination"]/li[not(@class="pagedown") and not(@class="jumpToPage")]/a[not(@class="a_jumpTo")]/@href'
        )
        if pages:
            #分页,过滤跳转
            for page in pages:
                # if pagination.extract() == response.request.url:
                #     yield self.parse_comments_data(response)
                # else:
                yield scrapy.Request(url=page.extract(),
                                     callback=self.parse_comments_data,
                                     dont_filter=True)
        else:
            yield scrapy.Request(url=response.request.url,
                                 callback=self.parse_comments_data,
                                 dont_filter=True)

    def parse_comments_data(self, response):
        select = scrapy.Selector(response=response)
        product = select.xpath(
            '//h1[@class="title J_title"]/text()').extract_first().strip()
        for comment in select.xpath(
                '//div[@class="tab_info" and @id="commentTabBlockNew"]/ul[@class="comment_listBox"]/li/div[@class="comment_conBox"]'
        ):
            dt = comment.xpath(
                './div[@class="comment_avatar_time "]/div[@class="time"]/meta/@content'
            ).extract_first()
            content = comment.xpath(
                './div[@class="comment_conWrap"]/div[@class="comment_con"]/p/span/text()'
            ).extract_first()
            item = SmzdmPhoneItem()
            item['product'] = product
            item['dt'] = dt
            item['content'] = content
            yield item