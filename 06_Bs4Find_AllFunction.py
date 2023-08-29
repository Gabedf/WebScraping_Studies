"""
This class teach about the function "find_all". This function can look for many different tags at the same time.
"""
import requests
from bs4 import BeautifulSoup
import re

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

"""
data = soup.find_all(['h4', 'a', 'p'])
print(data)

data = soup.find_all(string = 'Galaxy Tab 3') 
> It's going to look for all "Galaxy Tab 3" in data

data = soup.find_all(string = re.compile('Galaxy'))
> It's going to look for anything with "Galaxy"
"""
