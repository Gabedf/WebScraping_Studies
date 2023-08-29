"""
This class shows how to take specifics HTML tags;
"""

import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html')
print(soup.div)

