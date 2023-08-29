import requests
from bs4 import BeautifulSoup
import pandas as pd

# Variables initialization
bigger = 0
minor  = 0

names = []
prices = []
revs = []

for x in range(1, 61):
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=laptops&_sacat=5&rt=nc&_pgn='+str(x)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    name = soup.find_all('div', class_ = 's-item__title')
    price = soup.find_all('span', class_ = 's-item__price')
    rev = soup.find_all('div', class_ = 's-item__reviews')

    for i in name:
        a = i.text
        names.append(a)

    for i in price:
        a = i.text
        prices.append(a)

    for i in rev:
        a = i.text
        revs.append(a)

    if len(revs) < len(prices):
        a = int(len(prices)) - int(len(revs))
        for i in range(a):
            revs.append('Vazio')
    if len(names) < len(prices):
        a = int(len(prices)) - int(len(names))
        for i in range(a):
            names.append('Nome não encontrado')

df = pd.DataFrame({'Nomes produtos':names,
                   'Preços produtos':prices,
                   'Reviews produtos':revs
                   })

df.to_excel('C:\\Users\gabri\Desktop\TESTES\\Newebay.xlsm')