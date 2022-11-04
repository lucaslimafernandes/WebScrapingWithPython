from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon', timeout=10)
bsObj = BeautifulSoup(html, features='html.parser')

links = bsObj.find('div', {'id':'bodyContent'}).findAll(
                'a', href=re.compile('^(/wiki/)((?!:).)*$'))

for link in links:
    if 'href' in link.attrs:
        print(link.attrs['href'])
