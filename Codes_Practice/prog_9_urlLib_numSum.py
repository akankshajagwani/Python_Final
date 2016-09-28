# NO header content is read
import urllib
from BeautifulSoup import *

fhand = urllib.urlopen('http://python-data.dr-chuck.net/comments_246168.html')
html = fhand.read()
soup = BeautifulSoup(html)
tags = soup('span')
count = 0
sum = 0

for tag in tags:
    print tag.string
    sum =sum+ int(tag.contents[0])
    
print sum
    

    
