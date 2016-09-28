import re
# Regex_Pattern = r'^[aA]+$'   
Regex_Pattern = r'\b([aA])\1\1+\b'   
# Regex_Pattern = r'^[a]{,3}|[A]{}$'   
# Regex_Pattern = r'[a-z]*([a-z])\1' 
# Regex_Pattern = r'^([aA]+)\1([aA]+)\2$' 
obj = re.search(Regex_Pattern, raw_input())  
print obj
if obj is not None:
    print obj.group()
exit()
channel = open('Menu_regEx.txt')
data =channel.read()


Regex_Pattern = r'(.*)\b\nLow\b'
# lst = re.findall(Regex_Pattern ,data)
# print "lst:",lst
print (str(bool(re.search(Regex_Pattern, 'Steakburger'))).lower())
if len(Regex_Pattern) > 15:
	print "Warning : Length of regular expression greater than 15 characters."
    
    
