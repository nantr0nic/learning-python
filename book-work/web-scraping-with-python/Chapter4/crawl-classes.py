# This code from the "Web Scraping with Python" book doesn't work -- assumedly
# because the data/code from the example news articles has changed.
# I've used Democracy Now! and KGW sites instead. DistroWatch works too but
# the table is too much to figure out now. Body comes back as the entire page
# rather than the summary at the top of the article.


from bs4 import BeautifulSoup

# import requests
# curl_cffi helps dealing with 403's -- add 'impersonate="chrome"' attr to requests()
from curl_cffi import requests
import logging

# Setup logger.
logging.basicConfig(level=logging.INFO)

# Create a logger for this module.
logger = logging.getLogger(__name__)


class Content:
    """
    Common base class for all articles/pages.
    """

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Flexible printing function controls output.
        """
        print(f"URL: {self.url}")
        print(f"TITLE: {self.title}")
        print(f"BODY:\n{self.body}")


class Website:
    """
    Contains information about website structure.
    """

    # Allows making instances to call website information from rather than hard-coding.
    # Website object is instantiated from list at bottom of code.
    def __init__(self, name, url, titleTag, bodyTag):
        # name of site
        self.name = name
        # not the specific page being scraped
        self.url = url
        # tag for the title of the news article/page
        self.titleTag = titleTag
        # tag for the 'body' of the content to be scraped
        self.bodyTag = bodyTag


class Crawler:
    # Method to GET a page and return a BS object.
    def getPage(self, url):
        try:
            # using curl_cffi for requests
            req = requests.get(url, impersonate="chrome")
        except requests.exceptions.RequestException:
            logger.info(f"RequestException.{url}")
            return None
        # Return status code from GET request
        logger.info(f"getPage status code: {req.status_code}.")
        # getPage returns the BS object
        return BeautifulSoup(req.text, "html.parser")

    def safeGet(self, pageObj, selector):
        """
        Utility function used to get a content string from a
        Beautiful Soup object and a selector. Returns an empty
        string if no object is found for the given selector
        """
        
        # Using .select() instead of relying on key:value pair.
        # pageObj =  bs object, selector = a tag / CSS selector
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return "\n".join([elem.get_text() for elem in selectedElems])
        # If selector isn't found, return empty
        return ""

    def parse(self, site, url):
        """
        Extract content from a given page URL.
        """
        bs = self.getPage(url)
        # logging added for debug/tracking
        if bs is not None:
            logger.info(f"The BS object exists. {url}")
            title = self.safeGet(bs, site.titleTag)
            logger.info(f"Title tag detected. {title}")
            body = self.safeGet(bs, site.bodyTag)
            logger.info(f"Body tag detected. {body}")
            if title != "" and body != "":
                logger.info("The title and body are both not empty.")
                # if title/body exist in requested page, instantiate Content object
                content = Content(url, title, body)
                # print that shit
                content.print()

# instantiate Crawler object
crawler = Crawler()

# Website structures
siteData = [
    ["Democracy Now", "http://democracynow.org", "h1", "div.headline_summary"],
    # ["Distrowatch", "http://distrowatch.com", "td.rTitle", "td.rStory"],
    ["KGW", "http://www.kgw.com", "h1", "a.headline-list__title"],
]
websites = []

for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(
    websites[0],
    "https://www.democracynow.org/2024/12/13/headlines/mass_crowds_gather_for_first_friday_prayers_since_assad_ouster",
)
crawler.parse(websites[1], "https://www.kgw.com/local")

# crawler.parse(websites[1], "https://distrowatch.com/weekly.php?issue=current")

"""
def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, "html.parser")


def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find("h1").text
    lines = bs.find_all("p", {"class": "story-content"})
    body = "\n".join([line.text for line in lines])
    return Content(url, title, body)


def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find("h1").text
    body = bs.find("div", {"class", "post-body"}).text
    return Content(url, title, body)
    
url = "https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/"
content = scrapeBrookings(url)
print("Title: {}".format(content.title))
print("URL: {}\n".format(content.url))
print(content.body)

url = "https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html"
content = scrapeNYTimes(url)
print("Title: {}".format(content.title))
print("URL: {}\n".format(content.url))
print(content.body)
"""
