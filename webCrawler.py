import requests
import operator
from bs4 import BeautifulSoup as bs


def hulkpop_spider(maxPages):
    page = 1
    while page <= maxPages:
        print("\nPage " + str(page) + ":\n")

        sourceCode = requests.get("https://hulkpop.com/page/"+ str(page) + "/?s=")
        plainText = sourceCode.text
        soup = bs(plainText, features="html.parser")

        for link in soup.findAll('a', {'rel': 'bookmark'}):
            print(link.string)
            print(link.get("href") + "\n")
        page += 1

    print("\ndone! :)")


hulkpop_spider(int(input('how many pages? ')))
