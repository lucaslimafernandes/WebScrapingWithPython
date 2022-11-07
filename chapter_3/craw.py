from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen(f'http://en.wikipedia.org{pageUrl}')

    bsObj = BeautifulSoup(html, features='html.parser')
    links = bsObj.findAll('a', href=re.compile('^(/wiki/)'))
    for link in links:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')