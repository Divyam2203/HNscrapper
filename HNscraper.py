from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import pprint


def create_myhn():
    hn = []
    for s in range(1):
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


input = create_myhn()

# app = Flask(__name__)
# @app.route("/")
# def index(inp = None):
#     return render_template('index.html', list = inp)

# index(input)

pprint.pprint(sorted(create_myhn(), key=lambda k: k['points'], reverse=True))
