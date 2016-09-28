# https://www.hackerrank.com/challenges/a-super-hero
import time 
ticks_1 =  time.time()
def ConvertToInt(str):
    try:
        str = int(str)
        return str
    except:
        print "Non-integer input", str
        exit()
        
def CheckRange(num, minValue, maxValue):
    if num < minValue or  num > maxValue:
        print "Entry is not in range",num,".It should be >= %d and <= %d" %(minValue,maxValue)
        exit()

filePath = raw_input('File Path:') 
  
if len(filePath) <= 0: 
    filePath = "bullet_input.txt"
fhandle = open(filePath)

fhand_write = open("bullet_output.txt",'w')


line = fhandle.readline().strip()
T = line
# T = raw_input('')
T = ConvertToInt(T)
CheckRange(T,1,100)
MinBullets = []
for t in range(1,T+1):
    line = fhandle.readline().strip()
    NM = line
    # NM = raw_input('')
    lst_1 = NM.split()
    if len(lst_1) is 2:
        N = ConvertToInt(lst_1[0])
        CheckRange(N,1,100)
        M = ConvertToInt(lst_1[1])
        CheckRange(M,1,500000)
    else:
        print "N and M input wrong"
        exit()
    levels = range(1,N+1)
    enemies = range(0,M)
    P = {}    
    for n in levels:
        line = fhandle.readline().strip()
        P[n] = line
        # print len(line)
        # P[n] = raw_input('')
        P[n] = P[n].split()
        # print P[n]
        # print len(P[n]) is M
        # C = len(P[n])
        # if C is M:
            # print "entering"
        indx = 0
        for i in P[n]:
            i = ConvertToInt(i)
            CheckRange(i,1,1000)
            P[n][indx] =i
            indx = indx+1
        # else:
            # print "Invalid input, M:",M,"N: ",N,"len:",len(P[n]), type(M),type(len(P[n]))
            # exit()
    B = {}  
    for n in levels:
        
        line = fhandle.readline().strip()
        B[n] = line
        # B[n] = raw_input('')
        B[n] = B[n].split()
        # if len(B[n]) is M:
        indx = 0
        for i in B[n]:
            i = ConvertToInt(i)
            CheckRange(i,1,1000)
            B[n][indx] =i
            indx = indx+1
        # print B[1]  
        # else:
            # print "Invalid input, M:",M,"N: ",N
            # exit()
        
    # import numpy
    # DP = numpy.zeros(shape=(N,M), dtype=int)
    DP = {}
    DP[1] = []
    for i in enemies:
        # DP[0][i]=P[1][i]  
        # print i
        DP[1].append(P[1][i])  
        
    for i in range(2,N+1):
        DP[i] = []
        # fhand_write.write("DP[i-1]"+ str( DP[i-1])+"\n")
        # fhand_write.write( "B[i-1]"+str( B[i-1])+"\n")
        # rem = []
        # for kk in enemies:
            # rem.append((B[i-1][kk],DP[i-1][kk]))
        # fhand_write.write( "B[i-1],DP[i-1]"+str( rem)+"\n")
        # rem.sort()
        # fhand_write.write( "sorted"+str( rem)+"\n")
        # rem1 =  []
        # for j in enemies:
            # rem1.append((P[i][j],j))
        # rem1.sort()
        # fhand_write.write( "sorted P[i]"+str( rem1)+"\n")
        for j in enemies:
            bullet = []
            for k in enemies:
                if B[i-1][k] >= P[i][j] :               
                    # bullet.append(DP[i-2][k])
                    bullet.append(DP[i-1][k])
                else :
                    # bullet.append(DP[i-2][k]+P[i][j]-B[i-1][k])
                    bullet.append(DP[i-1][k]+P[i][j]-B[i-1][k])
            # DP[i-1][j]=min(bullet)
            DP[i].append(min(bullet))
        # fhand_write.write( "DP: "+str(DP[i])+str( min(DP[i]))+"\n")    
    # fhand_write.write( str(min(DP[N-1]))+"\n")      
    fhand_write.write( str(min(DP[N]))+"\n")      
    # print (min(DP[N-1]))     
    # print (min(DP[N]))       
    fhand_write.flush()
           
fhand_write.close() 
fhandle.close() 
ticks_2 =  time.time()
print "time: ",ticks_2-ticks_1