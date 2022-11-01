from pyexpat import features
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from time import sleep

def getTitle(url):

    try:
        html = urlopen(url)
        sleep(3)
    except HTTPError as e:
        return None
    
    try:
        bsObj = BeautifulSoup(html.read(), features=html.parser)
        title = bsObj.title
    except AttributeError as e:
        return None

    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')

if title == None:
    print('Title could not be found!')
else:
    print(title)