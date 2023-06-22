# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class UgamAmazonGeoSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UgamAmazonGeoDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        from w3lib.http import basic_auth_header
        import random
        lum_peoxy_set = {
            "lum-customer-c_11e7173f-zone-zone_us": "33p04eaqxtpu"
        }
        username, password = random.choice(list(lum_peoxy_set.items()))
        request.meta['proxy'] = "https://zproxy.lum-superproxy.io:22225"
        request.headers['Proxy-Authorization'] = basic_auth_header(username, password)

        # 58e54803a3ec8d911696b60bcd5ab666
        # 4c90a6838c880e80492c51eaac9734d3
        # 464938048fdd2618762acf8f15aeb62c
        # 906515bb5e2fc258287a8d77eadca36e
        # 3f48fb504397b218db65b5dae0ed175f
        # b2860ce65d5a8848361f31f2ffe0300a
        # 58e54803a3ec8d911696b60bcd5ab666
        # 62ad7228b732542539ab0ef9dc03129d
        # b2860ce65d5a8848361f31f2ffe0300a
        # ba8d17195ee5fa869a950bf05cd6fc61
        # 62af64de44353ae3b91ea6ec93234278

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
