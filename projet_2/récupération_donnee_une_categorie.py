import requests
from bs4 import BeautifulSoup
import time

# ---------------------------------------------------------------------------------------------------------------------#


def find_pages(url):
    url = url + 'index.html'
    reponse = requests.get(url=url)

    if reponse.ok:
        soup = BeautifulSoup(reponse.text, features="html.parser")
        page = soup.find("li", {"class": "current"})
        page = ''.join(page.findAll(text=True)).replace('Page 1 of ', '')
        page = int(page)
        print('Le nombre de page est de  : {}'.format(page))

    return page
# ---------------------------------------------------------------------------------------------------------------------#

def find_links(premiere_page, derniere_page, url_categorie):

    links = list()
    for i in range(premiere_page, derniere_page+1):
        if i == 1:
            url = url_categorie + 'index.html'
        else:
            url = url_categorie + "page-{}.html".format(str(i))

        link = "http://books.toscrape.com/catalogue/"
        reponse = requests.get(url=url)

        if reponse.ok:
            soup = BeautifulSoup(reponse.text, features="html.parser")
            articles = soup.find_all('article')
            print('Le nombre de  liens trouvés dans la  page {} est de  : {}'.format(i, len(articles)))
            for article in articles:
                article = article.find('a')
                link_book = article["href"].replace('../../../', '')
                links.append(link + link_book)
            time.sleep(1)
    print('Le nombre de  liens trouvés entre la page {} et la  page {} est de  : {}'.format(premiere_page, derniere_page, len(links)))

    return links

# ---------------------------------------------------------------------------------------------------------------------#


def get_informations(link):

    informations = ''
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
        article = soup.find("article", {"class": "product_page"}).findAll('p')[3]
        product_description = ''.join(article.findAll(text=True)).replace(';', '.')
        image = soup.find('img')
        link_image = image["src"].replace('../../', 'http://books.toscrape.com/')
        print('title :', title)
        '''
        print(
            'universal_product_code :', universal_product_code, '\n',
            'title :', title, '\n',
            'price_including_tax :', price_including_tax, '\n',
            'price_excluding_tax :', price_excluding_tax, '\n',
            'price_excluding_tax :', price_excluding_tax, '\n',
            'number_available :', number_available, '\n',
            'product_description :', category, '\n',
            'review_rating :', review_rating, '\n',
            'link_image :', link_image
        )
        '''
        informations = universal_product_code \
                       + ';' + title \
                       + ';' + price_including_tax \
                       + ';' + price_excluding_tax \
                       + ';' + number_available \
                       + ';' + product_description \
                       + ';' + category \
                       + ';' + review_rating \
                       + ';' + link_image

        time.sleep(1)
    return informations


# ---------------------------------------------------------------------------------------------------------------------#

url = 'http://books.toscrape.com/catalogue/category/books/default_15/'
nombre_page = find_pages(url)
# find links for all books
links = find_links(premiere_page=1, derniere_page=nombre_page, url_categorie=url)
# écrire les liens dans  un fichier text
with open('linkss.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')

# read txt file
with open('linkss.txt', 'r') as file_txt:
    # write csv file
    with open('books_information.csv', 'w', encoding='utf-8') as file_csv:
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

