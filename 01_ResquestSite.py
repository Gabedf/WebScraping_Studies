"""
Class that explain how to use the basics of "Requests" library.
"""

import requests

url = "https://www.amazon.com.br/Amazfit-GTS-Mini-Modelo-meia-noite/dp/B09Z6GMPC6/"
r = requests.get(url)

# print(r.status_code)

print(r.text)
# Basically, this function is going to print (or take) the HTML from the website.
