# Copy pasting the classes from crawl-classes to save my wrists.
# REFACTOR THIS SHIT AND PUT CLASSES INTO SEPARATE FILE.

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

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Flexible printing function controls output.
        """
        print(f"New article found for topic: {self.topic}")
        print(f"URL: {self.url}")
        print(f"TITLE: {self.title}")
        print(f"BODY:\n{self.body}")


class Website:
    """
    Contains information about website structure.
    """

    # Allows making instances to call website information from rather than hard-coding.
    # Website object is instantiated from list at bottom of code.
    def __init__(
        self,
        name,
        url,
        searchUrl,
        resultListing,
        resultUrl,
        absoluteUrl,
        titleTag,
        bodyTag,
    ):
        # name of site
        self.name = name
        # not the specific page being scraped
        self.url = url
        # base search URL to append string to...
        self.searchUrl = searchUrl
        # the tag of the result listing
        self.resultListing = resultListing
        # the tag of the result link
        self.resultUrl = resultUrl
        # bool for whether search result links are absolute or not
        self.absoluteUrl = absoluteUrl
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
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ""
        """
        # Using .select() instead of relying on key:value pair.
        # pageObj =  bs object, selector = a tag / CSS selector
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return "\n".join([elem.get_text() for elem in selectedElems])
        # If selector isn't found, return empty
        return ""
        """

    def search(self, topic, site):
        """
        Searches a given website for a given topic and records all pages found.
        """
        # getPage with search url query + topic keyword passed as an attribute
        bs = self.getPage(site.searchUrl + topic)
        logger.info(f"getPage({site.searchUrl} + {topic}) success.")
        # use BS to select the tag(s) of the search results and make them into an object
        searchResults = bs.select(site.resultListing)
        # for loop for each result
        for result in searchResults:
            # assign search result href links to url var
            logger.info(f"site.resultUrl is {site.resultUrl}")
            url = result.select(site.resultUrl)[0].attrs["href"]
            # Check to see whether it's a relative or an absolute URL
            # If absolute, use url
            if site.absoluteUrl:
                bs = self.getPage(url)
                logger.info("Absolute!")
            else:
                # if relative, use netloc url + the relative path of the result
                bs = self.getPage(site.url + url)
                logger.info("Relative!")
            if bs is None:
                logger.info(
                    "Something was wrong with that page or URL. Skipping!"
                )
                return
            title = self.safeGet(bs, site.titleTag)
            logger.info(f"Got title. -->  {title}")
            body = self.safeGet(bs, site.bodyTag)
            logger.info(f"Got body. --> {body}")
            if title != "" and body != "":
                content = Content(topic, title, body, url)
                content.print()


crawler = Crawler()

siteData = [
    [
        "Linux Today",
        "https://www.democracynow.org",
        "https://www.democracynow.org/search?utf8=%E2%9C%93&query=",
        "div.content",
        "a",
        False,
        "h1",
        "div.content",
    ],
]

sites = []
for row in siteData:
    sites.append(
        Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    )

topics = ["israel"]
for topic in topics:
    print("GETTING INFO ABOUT: " + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)
