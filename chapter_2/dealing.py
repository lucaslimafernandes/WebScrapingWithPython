from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, features='html.parser')


#dealing with siblings
for sibling in bsObj.find('table', {'id':'giftList'}).tr.next_siblings:
    #print(sibling)
    pass


#dealing with your parents
par = bsObj.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
print(par)



#finally-done
