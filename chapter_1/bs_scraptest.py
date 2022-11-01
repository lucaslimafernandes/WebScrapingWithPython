from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen('http://pythonscraping.com/pages/page1.html')

bsObj = bs(html.read())

print(bsObj.h1)

try:
    badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print('Tag was not found')
else:
    if badContent == None:
        print('Tag was not found!')
    else:
        print(badContent)
