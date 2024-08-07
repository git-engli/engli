
from bs4 import BeautifulSoup
import requests

source = requests.get('*{url}*').text
soup = BeautifulSoup(source, 'lxml')

# Find and print all paragraph text
for p in soup.find_all('p'):
    print(p.get_text())


import scrapy

class BlogSpider(scrapy.Spider):
    name = '*{spider_name}*'
    start_urls = ['*{starting_url}*']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)



from selenium import webdriver

# Initialize webdriver (make sure the chromedriver is in PATH)
driver = webdriver.Chrome()

# get source code
driver.get('*{url}*')

# Print the title of the webpage
print(driver.title)

driver.quit()



python bs4_scrape.py
python scrapy_spider.py
python selenium_scrape.py