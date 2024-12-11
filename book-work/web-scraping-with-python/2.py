from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, "html.parser")

"""
Various examples from the book:
for child in bs.find("table", {"id":"giftList"}).children:
    print(child)
    
for descendent in bs.find("table", {"id":"giftList"}).descendants:
    print(descendent)

for sibling in bs.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)
"""
# regex section v
# ../img/gifts/img3.jpg
"""
images = bs.find_all("img", {"src":re.compile("\.\./img/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])
    
print("Second regex below")
images = bs.find_all("img", {"src":re.compile("\.\./img/gifts/img[0-9]+\.jpg")})
for image in images:
    print(image["src"])
"""
# lambda functions V
for instance in bs.find_all(lambda tag: len(tag.attrs) == 2):
    print(instance)