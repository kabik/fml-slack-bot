import requests
from bs4 import BeautifulSoup

TOP_URL = 'https://www.fmylife.com'
RANDOM_URL = TOP_URL + '/random'
RETRY = 5

for i in range(RETRY):
    html = requests.get(RANDOM_URL).text
    soup = BeautifulSoup(html, 'html.parser')

    article = soup.article.select('article a.article-link')[0]
    article_string = article.string
    article_link = TOP_URL + article.get('href')

    if article_string: break

print(article)
print(article_string)
print(article_link)
