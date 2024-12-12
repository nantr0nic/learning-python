from urllib.request import urlopen, Request
from urllib.parse import urlparse
import urllib.error
from bs4 import BeautifulSoup
import re
import datetime
import time
import random
import logging

random.seed(int(datetime.datetime.now().timestamp()))

# Setup logging
logging.basicConfig(level=logging.INFO)


# Retrieves a list of all Internal links found on a page.
def getInternalLinks(bs, includeUrl):
    includeUrl = "{}://{}".format(
        urlparse(includeUrl).scheme, urlparse(includeUrl).netloc
    )
    internalLinks = []
    # Finds all links that begin with a "/"
    for link in bs.find_all("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                if link.attrs["href"].startswith("/"):
                    internalLinks.append(includeUrl + link.attrs["href"])
                else:
                    internalLinks.append(link.attrs["href"])
    return internalLinks


# Retrieves a list of all external links found on a page.
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    # Finds all links that start with "http" that do not contain the current URL
    for link in bs.find_all(
        "a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")
    ):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks


def getRandomExternalLink(startingPage, visited):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        req = Request(startingPage, headers=headers)
        html = urlopen(req).read()
        bs = BeautifulSoup(html, "html.parser")
        externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)

        if len(externalLinks) == 0:
            logging.warning("No external links, looking around the site for one.")
            domain = "{}://{}".format(
                urlparse(startingPage).scheme, urlparse(startingPage).netloc
            )
            internalLinks = getInternalLinks(bs, domain)

            # If no internal or external links are found, return the starting page
            if len(internalLinks) == 0:
                logging.warning("No more links to follow. Returning to previous link.")
                if visited:
                    return getRandomExternalLink(visited[-1], visited[:-1])
                else:
                    return None
            else:
                visited.extend(internalLinks)
                return getRandomExternalLink(
                    internalLinks[
                        random.randint(0, min(len(internalLinks), len(visited)) - 1)
                    ],
                    visited,
                )
        else:
            time.sleep(random.uniform(2, 5))  # Pause to not be a dick / get in trouble
            return externalLinks[random.randint(0, len(externalLinks) - 1)]
    except urllib.error.HTTPError as e:
        logging.error(f"HTTP Error: {e.code}")
        return None
    except urllib.error.URLError as e:
        logging.error(f"URL Error: {e.reason}")
        return None


def followExternalOnly(startingSite):
    visited = [startingSite]
    while True:
        try:
            externalLink = getRandomExternalLink(startingSite, visited)
            if externalLink is not None and externalLink not in visited:
                print(f"Random external link is: {externalLink}")
                logging.info(f"Followed external link to: {externalLink}")
                followExternalOnly(externalLink)
            else:
                continue
        except urllib.error.HTTPError as e:
            logging.error(f"HTTP Error: {e.code}")
            return None
        except urllib.error.URLError as e:
            logging.error(f"URL Error: {e.reason}")
            return None


# Main function to start the process
def main():
    startingSite = "http://www.civitai.com"
    followExternalOnly(startingSite)


if __name__ == "__main__":
    main()
