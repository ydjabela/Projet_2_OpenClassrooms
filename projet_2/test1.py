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

def get_informations(link):

    reponse = requests.get(url=link)
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, features="html.parser")

        title = soup.select('h1')[0].text.strip()
        universal_product_code = soup.select('td')[0].text.strip()
        category = soup.select('td')[1].text.strip()
        price_excluding_tax = soup.select('td')[2].text.strip()
        price_including_tax = soup.select('td')[3].text.strip()
        number_available = soup.select('td')[5].text.strip()
        review_rating = soup.select('td')[6].text.strip()
        product_description = '1'
        image = soup.find('img')
        link_image = image["src"]

        print( 'universal_product_code :', universal_product_code)
        print('title :', title)
        print('price_including_tax :', price_including_tax)
        print('price_excluding_tax :', price_excluding_tax)
        print('number_available :', number_available)
        print('product_description :', category)
        print('review_rating :', review_rating)
        print('link_image :', link_image)
        informations = universal_product_code \
                       + ';' + title \
                       + ';' + price_including_tax \
                       + ';' + price_excluding_tax \
                       + ';' + number_available \
                       + ';' + product_description \
                       + ';' + category \
                       + ';' + review_rating \
                       + ';' + link_image

        print(informations)
        time.sleep(1)
    return informations


# ---------------------------------------------------------------------------------------------------------------------#
# http://books.toscrape.com/catalogue/the-white-cat-and-the-monk-a-retelling-of-the-poem-pangur-ban_865/index.html
url = 'http://books.toscrape.com/catalogue/worlds-elsewhere-journeys-around-shakespeares-globe_972/index.html'
informations = get_informations(link=url)
'''
links = find_links()

with open('linkss.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')

# read txt file
with open('linkss.txt', 'r') as file_txt:
    # write csv file
    with open('books_information.csv', 'w') as file_csv:
        # entete
        file_csv.write(
            'product_page_url;universal_ product_code (upc);title;price_including_tax;price_excluding_tax;number_available;product_description;category;review_rating;image_url\n'
        )
        for link in file_txt:
            # Supprimer le saut a la  ligne
            url = link.strip()
            # get  information for each link on  the txt  file
            try:
                informations = get_informations(link=url)
                # write all information on csv file
                file_csv.write(url + ';' + informations + '\n')
            except:
                print('except in  link : ' + link)
'''

