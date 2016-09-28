# NO header content is read
import urllib
# fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
fhand = urllib.urlopen('https://www.coursera.org/learn/python-network-data/lecture/UxIOc/lets-write-a-web-browser')
data = fhand.read()
print data
count = dict()
data = data.split('/n')

for line in data:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) +1 

print count
