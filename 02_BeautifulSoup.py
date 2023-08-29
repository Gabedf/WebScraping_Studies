"""
Class that teach how to extract HTML using bs4 and pass to Python. After this class will be important because will
help to use bs4 functions.
OBS: use a website specific to web scraping learning (the URL is a good example).
"""

import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html')
print(soup)
