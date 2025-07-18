# Scrapy settings for rv_backup project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "rv_backup"

SPIDER_MODULES = ["rv_backup.spiders"]
NEWSPIDER_MODULE = "rv_backup.spiders"

# ❌ Amazon blocks bots: we set obey robots.txt to False
ROBOTSTXT_OBEY = False

# ✅ Delay to avoid rate limiting (important for Amazon)
DOWNLOAD_DELAY = 2

# ✅ scrapy-selenium middleware must be enabled
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800,
}

# ✅ scrapy-selenium: specify driver type and path to ChromeDriver
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = r"C:\Users\Lhynzkie\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
SELENIUM_DRIVER_ARGUMENTS = ['--headless', '--no-sandbox', '--disable-gpu']

# ✅ Output format
FEED_FORMAT = "json"
FEED_URI = "results.json"

# 🛡️ Optional (useful when Amazon blocks bots quickly)
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# ✅ Future-proof and compatibility settings
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
