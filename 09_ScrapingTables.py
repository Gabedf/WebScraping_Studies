import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://valorinveste.globo.com/cotacoes/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find_all('tbody', class_ = 'vd-table__body')

lista = []

for i in table:
    x = i.string
    lista.append(x)

print(lista)