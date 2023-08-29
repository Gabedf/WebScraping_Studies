import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
price = soup.find_all('h4', {'class':'pull-right price'})
desc = soup.find_all('p', {'class':'description'})

for i in price:
    print('PREÇO:', i.string)

