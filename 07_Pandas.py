import requests
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

names = soup.find_all('a', class_ = 'title')
namesProducts = []

prices = soup.find_all('h4', class_ = 'pull-right price')
pricesProducts = []

desc = soup.find_all('p', class_ = 'description')
descProducts = []

for i in names:
    names = i.string
    namesProducts.append(names)

for i in prices:
    prices = i.string
    pricesProducts.append(prices)

for i in desc:
    desc = i.string
    descProducts.append(desc)

df = pd.DataFrame({'Product Names':namesProducts,'Product Prices':pricesProducts,'Description Product':descProducts})
df.to_excel('C:\\Users\gabri\Desktop\TESTES\Produtos.xlsx')

print(df)
