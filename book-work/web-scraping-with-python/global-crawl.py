from urllib.request import urlopen  # library for requesting URL
from urllib.parse import urlparse
from bs4 import BeautifulSoup  # parser and scraping functions
import re  # used to evaluate regex
import datetime  # used to help generate random seed
import random  # used to pick links at random from list

pages = set()  # seems to be unused in this script
random.seed(
    int(datetime.datetime.now().timestamp())
)  # generate random seed based on timestamp


# Retrieves a ist of all internal links found on a page.
def getInternalLinks(bs, includeUrl):
    # urlparse(url).scheme is passed to the first brackets to parse the "http", "https", part of the url
    # urlparse(url).netloc in the second brackets returns the network location part of the url
    # scheme = "https" then :// then netloc = "www.example.com"
    includeUrl = "{}://{}".format(
        urlparse(includeUrl).scheme, urlparse(includeUrl).netloc
    )
    internalLinks = []
    # Finds all links that begin with a "/"
    # re.compile() compiles a regular expression pattern into a regex object to be re-used efficiently
    #   rather than be re-parsed every time
    # regex pattern is ["^(/|.*" + includeUrl + ")"] instead of [includeUrl + "^(/|.*)"]
    #   because it will capture relative paths in addition to absolute internal links.
    for link in bs.find_all("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        # make sure link isn't empty
        if link.attrs["href"] is not None:
            # make sure link isn't already in internalLinks list
            if link.attrs["href"] not in internalLinks:
                if link.attrs["href"].startswith("/"):
                    # if link is relative, append it to the internalLinks list with the whole url
                    internalLinks.append(includeUrl + link.attrs["href"])
                else:
                    # if link is absolute, append it as is
                    internalLinks.append(link.attrs["href"])
    # returns the list of internal links found in includeUrl
    return internalLinks  
    


# Retrieves a list of all external links found on a page.
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    # Finds all links that start with "http" that do not contain the current url.
    for link in bs.find_all(
        "a", href=re.compile("^(http|https|www)((?!" + excludeUrl + ").)*$")
    ):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks


def getRandomExternalLink(startingPage):
    # urlopen(url) sends an HTTP request to the specified url. The server responds and a connection is made.
    # it also send a request to the server which responds with the requested data across made connection.
    # urlopen() contains: the URL, the HTTP status code, headers, the actual data from the server.
    html = urlopen(startingPage)
    # BeautifulSoup is the library that interprets the data given by urllib by parsing it (in this case as HTML)
    # it provides functions for working with the data, such as finding tags and turning them into objects etc.
    bs = BeautifulSoup(html, "html.parser")
    # get external links, pass the html object (bs) and the startingpage to getExternalLinks
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    # What to do if there aren't any external links in the list.
    if len(externalLinks) == 0:
        print("No external links, looking around the site for one.")
        # get string for whatever url the crawler is currently on
        domain = "{}://{}".format(
            urlparse(startingPage).scheme, urlparse(startingPage).netloc
        )
        # pass domain to getInternalLinks to search for external links
        internalLinks = getInternalLinks(bs, domain)
        # return a (random) external link from the list
        ### What if it only finds 1 external link? Index error?
        # Had to modify this section because of index errors. If no internal links, just start again.
        if len(internalLinks) >= 1:
            print("internalLinks is >= 1")
            return getRandomExternalLink(internalLinks[0])
        elif len(internalLinks) == 0:
            print("internalLinks == 0")
            return followExternalOnly("http://oreilly.com")
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]
    
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: {}".format(externalLink))
    followExternalOnly(externalLink)

# Collects a list of all external URLs found on the site.
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = "{}://{}".format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)
    
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)


def main():
    # followExternalOnly("http://oreilly.com")
    allIntLinks.add("http://oreilly.com")
    getAllExternalLinks("http://oreilly.com")

if __name__ == "__main__":
    main()
