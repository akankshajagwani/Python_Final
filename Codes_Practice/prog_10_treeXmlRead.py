import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_246165.xml '
uh = urllib.urlopen(serviceurl)

   
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)

sum = 0
results = tree.findall('comments/comment')

for result in results: 
    
    sum =sum+ int(result.find('count').text)



print 'sum:',sum



serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'eate
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location