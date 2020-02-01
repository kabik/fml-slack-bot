import requests
import json
import os
from bs4 import BeautifulSoup

import translate

TOP_URL = 'https://www.fmylife.com'
RANDOM_URL = TOP_URL + '/random'
RETRY = 5
WEBHOOK_URL = os.environ['WEBHOOK_URL']

def lambda_handler(event, context):
    post_slack()
    return {
        'statusCode': 200,
        'body': json.dumps('DONE')
    }

def post_slack():
    for i in range(RETRY):
        html = requests.get(RANDOM_URL).text
        soup = BeautifulSoup(html, 'html.parser')

        article = soup.article.select('article a.article-link')[0]
        article_ja = article.string.strip()
        article_link = TOP_URL + article.get('href')

        if article_ja: break

    article_en = translate.translate(article_ja)

    print('article_ja = \"{}\"'.format(article_ja))
    print('article_en = \"{}\"'.format(article_en))
    print('article_link = \"{}\"'.format(article_link))

    message_json = {"text": "{}\n----\n{}\n{}".format(article_ja, article_en, article_link)}
    res = requests.post(
        WEBHOOK_URL,
        json.dumps(message_json),
        headers={'Content-Type': 'application/json'})

    print(res)

translate.translate('は')
