# User input: hrs and rate, computing pay
# Queries, 1. how to break and return? Ans: exit()2. in if condition how to use and or? Ans: and
# raw_input always return string type

def computePay(hrs,rate):
    if hrs <= 40 :
        pay = hrs*rate
    else:
        pay = (hrs-40)*(1.5*rate) + 40*rate

    print "Gross Pay: %0.2f  at the rate of %0.2f for %0.2f hours" %(pay,rate,hrs)

    if pay > 100:
        print "higher pay"
    else:
        print "lower pay"
        
    if hrs >= 40:
        print "over work"
    else:
        print "nice, you work for less hours"  



try:
    hrs = (raw_input("Enter Hours:"))
    hrs = float(hrs)
    rate = float(raw_input("Enter Rate per hour:"))
    rate = float(rate)
        
except: 
    print "Error: User entered a non-numeric value."
    exit()
 
computePay(hrs,rate)
   
