import json
import urllib
# url = raw_input('Enter Url-')
# url = 'http://python-data.dr-chuck.net/comments_42.json'
url = 'http://python-data.dr-chuck.net/comments_246169.json'
fhand = urllib.urlopen(url)

data = fhand.read()


info = json.loads(data)

print 'User count:', len(info['comments'])
count = 0;
sum = 0;
for item in info['comments']:
   
    count = count+1
    sum =sum+item['count']

print 'sum:',sum