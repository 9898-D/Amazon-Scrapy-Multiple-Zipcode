# Scrapy settings for ugam_amazon_geo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ugam_amazon_geo'

SPIDER_MODULES = ['ugam_amazon_geo.spiders']
NEWSPIDER_MODULE = 'ugam_amazon_geo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ugam_amazon_geo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ugam_amazon_geo.middlewares.UgamAmazonGeoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'ugam_amazon_geo.middlewares.UgamAmazonGeoDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ugam_amazon_geo.pipelines.UgamAmazonGeoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# DOWNLOADER_MIDDLEWARES = {'scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware': 610}

# DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 300}
# CRAWLERA_ENABLED = True
# # CRAWLERA_APIKEY = '35fd38500133452f9cedb495a2c83c89'
# # CRAWLERA_APIKEY = 'a97febde5ba54db99578d67b0c65eeac'
# CRAWLERA_APIKEY = 'e58e322ad9044d9c8321637ac5a02bc3'
# # CRAWLERA_APIKEY = '3eaa40819cd34d06a59815c4fa208a18'
# ONCURRENT_REQUESTS = 1
# CONCURRENT_REQUESTS_PER_DOMAIN = 1
# AUTOTHROTTLE_ENABLED = False
# DOWNLOAD_TIMEOUT = 1.25

# 93457f2cf35c4eb18c45893789c97447
# 3f3e507d03dd42bea2ffbebd8d75a847
# ac3cd341c6894dc7abef05c8816131ed
# 191c71373cd3427f930acab48d526bf1
# 0cd6bc70-7755-11eb-bb39-af744d2ad613
# 748d8db95b9147f8b7cdcaadc471cf53
# cb317a6615984f0f8b172ca650e73330
# 85e35c511b7f4dc8a725799ce6e3c274
# ffb2bdd0cae44a18a2262a854be2e665
