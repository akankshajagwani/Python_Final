import re
channel = open('regex_sum_246163.txt')
data =channel.read()
lst = re.findall('[0-9]+' ,data)
addition = 0
for num in lst:
        
        num = int(num)
        addition = num+addition
print addition
exit();

