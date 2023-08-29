import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

price = soup.find('h4', {'class':'pull-right price'})
# price = soup.find('h4', _class = 'pull-right price') / It could be done in that way
print(price.string)

desc = soup.fin('p', {'class':'description'})
print(desc.string)

