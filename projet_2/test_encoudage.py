import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/the-republic_78/index.html'

content = requests.get(url)
if content.ok:
    soup = BeautifulSoup(content.text, features="html.parser")
    # option 1
    price_excluding_tax = soup.select('td')[2].text.encode('utf-8')
    print(str(price_excluding_tax))
