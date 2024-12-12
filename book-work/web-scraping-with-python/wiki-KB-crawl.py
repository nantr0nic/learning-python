# This will crawl Wikipedia. It starts with the Kevin Bacon article, picks a random article link,
# prints the article name, follows that link, picks another random article link, and so on.
# This is following the book "Web Scraping with Python"

from operator import rshift
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import datetime
import random
import re

# I added init_seed and load_seed for fun and to practice reusing the same seeds.


def init_seed():
    with open("seed.json", "w") as f:
        json.dump({"seed": int(datetime.datetime.now().timestamp())}, f)
        print("Initialized.")
    with open("seed.json", "r") as f:
        data = json.load(f)
        print(f"Using: {data['seed']}")
        return data["seed"]


def load_seed():
    try:
        with open("seed.json", "r") as f:
            data = json.load(f)
            return data["seed"]
    except FileNotFoundError:
        print("No saved seed found. Initializing with a new one.")
        init_seed()


# Load the seed
seed = load_seed()

random.seed(seed)

print(f"Seed: {seed}")


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org{}".format(articleUrl))
    bs = BeautifulSoup(html, "html.parser")
    return bs.find("div", {"id": "bodyContent"}).find_all(
        "a", href=re.compile("^(/wiki/)((?!:).)*$")
    )


links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)


"""
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bs = BeautifulSoup(html, "html.parser")

# print all links:
for link in bs.find_all("a"):
    if "href" in link.attrs:
        print(link.attrs["href"])
"""

"""
# print specific (article) links:
for link in bs.find("div", {"id": "bodyContent"}).find_all(
    # the book's regex example was "^(/wiki/)((?!:).)*$" but this returns more than
    # first_last name article links. The bottom regex is more restrictive.
    "a",
    href=re.compile("^(/wiki/)[a-zA-Z0-9]*_[a-zA-Z0-9]*$"),
):
    if "href" in link.attrs:
        print(link.attrs["href"])
"""
