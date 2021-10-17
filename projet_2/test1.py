import requests
from bs4 import BeautifulSoup
import time

# ---------------------------------------------------------------------------------------------------------------------#


def find_links():
    links = list()
    for i in range(1, 2+1):
        print("Page : ", str(i))

        if i == 1:
            link = url = "http://books.toscrape.com/"
        else:
            url = "http://books.toscrape.com/catalogue/page-{}.html".format(str(i))
            link = "http://books.toscrape.com/catalogue/"

        reponse = requests.get(url=url)

        if reponse.ok:
            soup = BeautifulSoup(reponse.text, features="html.parser")
            articles = soup.find_all('article')
            print(len(articles))
            for article in articles:
                article = article.find('a')
                link_book = article["href"]
                links.append(link + link_book)
            time.sleep(1)
        print(len(links))

    return links

# ---------------------------------------------------------------------------------------------------------------------#

def get_informations(links):

    url = "http://books.toscrape.com/catalogue/worlds-elsewhere-journeys-around-shakespeares-globe_972/index.html"
    reponse = requests.get(url=url)
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, features="html.parser")
        #universal_product_code = soup.find('article')

        title = soup.select('h1')[0].text.strip()
        print(str(title))


# ---------------------------------------------------------------------------------------------------------------------#


links = find_links()
get_informations(links=links)
with open('linkss.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')

