import requests
from bs4 import BeautifulSoup


links = list()
for i in range(1, 50+1):
    print(i)

    if i == 1:
        url = "http://books.toscrape.com/"
    else:
        url = "http://books.toscrape.com/catalogue/page-{}.html".format(str(i))
    reponse = requests.get(url=url)
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, features="html.parser")
        articles = soup.find_all('article')
        print(len(articles))
        for article in articles:
            article = article.find('a')
            link = article["href"]
            links.append("http://books.toscrape.com/" + link)

    print(links)



