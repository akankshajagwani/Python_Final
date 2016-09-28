input1 =raw_input("Please enter an integer: ")
try:
    intVal =int(input1)
    print "input1: ",intVal
except:
    intVal = -1
    print "Invalid Input:  ",input1,intVal

