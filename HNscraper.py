import requests
from bs4 import BeautifulSoup
import pprint


def create_myhn():
    hn = []
    for s in range(10):
        res = requests.get("https://news.ycombinator.com/news?p={s}")
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titleline > a')
        subtexts = soup.select('.subtext')
        for i, item in enumerate(links):
            title = links[i].getText()
            href = links[i].get('href')
            vote = subtexts[i].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(" points", ""))
                hn.append({"title": title, "link": href, "points": points})
            else:
                hn.append({"title": title, "link": href, "points": 0})

    return hn


pprint.pprint(create_myhn())
