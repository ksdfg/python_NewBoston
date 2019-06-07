import requests
from bs4 import BeautifulSoup as bs


def hulkpop_spider(toSearch, max):
    page = 1
    itemNo = 0

    while True:
        soup = bs(requests.get("https://hulkpop.com/page/" + str(page) + "/?s=" + str(toSearch).replace(" ", "+")).text, features="html.parser")
        if len(soup.select("h2 a")) == 0:
            break

        for link in soup.select("h2 a"):
            itemNo += 1
            if itemNo > int(max):
                print("\ndone! :)")
                return

            print("\n" + str(itemNo) + ". " + link.string, link.get("href"), sep='\n')

            subSoup = bs(requests.get(link.get("href")).text, features="html.parser")
            for i in subSoup.findAll('p'):
                if str(i)[3:8] == "TRACK":
                    print(str(i).replace("<p>", "").replace("<br/>", "")[:-4])
                    break

        page += 1

    print("\ndone! :)")


hulkpop_spider(input('\nwhat to search? '), input('how many results? '))

