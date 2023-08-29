"""
Class about how to go to the next pages using BeatifulSoup and Requests library.
"""

import requests
from bs4 import BeautifulSoup

for i in range(1, 5):
    url = 'https://webscraper.io/test-sites/e-commerce/static/computers/tablets?page='+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    np = soup.find('li', class_ = 'next page').get('href')
    print(url)

