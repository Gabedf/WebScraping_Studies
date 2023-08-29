import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://valorinveste.globo.com/cotacoes/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tables = soup.find('div', class_ = 'vd-table')
header = tables.find_all('thead', class_ = 'vd-table__head')
titles = []

name = tables.find('tbody', class_ = 'vd-table__body')
names = []

"""
for i in header:
    a = i.text
    titles.append(a)
"""

"""
OBS: ESTUDAR PARA DESCOBRIR COMO FAZER ISSO
"""