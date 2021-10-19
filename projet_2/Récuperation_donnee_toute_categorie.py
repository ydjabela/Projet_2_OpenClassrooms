import requests
from bs4 import BeautifulSoup
import time


# ---------------------------------------------------------------------------------------------------------------------#

def find_books_categorie(url):
    urls_categories = list()
    reponse = requests.get(url=url)

    if reponse.ok:
        soup = BeautifulSoup(reponse.text, features="html.parser")
        categories = soup.find('ul', {"class": "nav"})
        categories = categories.select('li')
        print('Le nombre de  catégorie trouvés est de  : {}'.format(len(categories)))
        for categorie in categories:
            categorie_a = categorie.find('a')
            link_categorie = categorie_a["href"]
            urls_categories.append(url + link_categorie)
        time.sleep(1)

    return urls_categories

# ---------------------------------------------------------------------------------------------------------------------#


def find_pages(url_categorie):
    url = url_categorie
    reponse = requests.get(url=url)

    if reponse.ok:
        soup = BeautifulSoup(reponse.text, features="html.parser")
        page = soup.find("li", {"class": "current"})
        if page:
            page = ''.join(page.findAll(text=True)).replace('Page 1 of ', '')
            page = int(page)
        else:
            page = 1
        print('Le nombre de page est de  : {}'.format(page))

    return page
# ---------------------------------------------------------------------------------------------------------------------#

def find_books_links(premiere_page, derniere_page, url_categorie):

    links = list()
    for i in range(premiere_page, derniere_page+1):
        if i == 1:
            url = url_categorie
        else:
            url = url_categorie.replace('index.html', "page-{}.html".format(str(i)))

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

to_update = str(input("Do  you need to update the  links or categorie Y|N ? "))
if to_update in('Y', 'y'):
    url = 'http://books.toscrape.com/'
    # chercher  toutes les categories des  livres de  url
    urls_categories = find_books_categorie(url=url)

    for i in range(1, len(urls_categories)):
        url_categorie = urls_categories[i]
        print(url_categorie)
        # Chercher le  nombre de  page de chaque catégorie
        nombre_pages = find_pages(url_categorie=url_categorie)

        # find links for all books de la catégorie
        links = find_books_links(premiere_page=1, derniere_page=nombre_pages, url_categorie=url_categorie)

        # écrire les liens dans  un fichier text
        with open('categorie {} links.txt'.format(i), 'w') as file:
            for link in links:
                file.write(link + '\n')

else:
    for i in range(1, 50+1):
        # read txt file et search information for each book link
        with open('categorie {} links.txt'.format(i), 'r') as file_txt:
            # write csv file
            with open('books_information categorie {}.csv'.format(i), 'w', encoding='utf-8') as file_csv:
                # entete
                file_csv.write(
                    'product_page_url;'
                    'universal_ product_code (upc);'
                    'title;'
                    'price_including_tax;'
                    'price_excluding_tax;'
                    'number_available;'
                    'product_description;'
                    'category;review_rating;'
                    'image_url\n'
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
                        print('except at  link : ' + link)


