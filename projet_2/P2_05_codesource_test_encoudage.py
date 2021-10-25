import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/the-republic_78/index.html'

reponse = requests.get(url=url)
reponse.encoding = "utf-8"
if reponse.ok:
    soup = BeautifulSoup(reponse.text, features="html.parser")
    # option 1
    price_excluding_tax = soup.select('td')[2].text
    print(str(price_excluding_tax))
