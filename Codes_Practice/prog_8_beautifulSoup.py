
# make sure BeautifulSoup.py file exists in the same directory
import urllib
from BeautifulSoup import *


pos = raw_input('Enter Position-')
pos =int(pos)
rep = raw_input('Enter Count-')
rep = int(rep)
# url = 'http://python-data.dr-chuck.net/known_by_Lyndsay.html'
url = raw_input('Enter url-')
name_1 = Default
for i in range(1,rep+1):
    # print url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    count =0
    tags =soup('a')
    for tag in tags:
        
        count =count+1
        
        if count == pos:
            url = tag.get('href', None)
            
            name_1 = tag.text
            
            if url == None:
                break
            break

print name_1