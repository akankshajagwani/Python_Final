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

fhand_write = open("bullet_output_2.txt",'w')


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
        # P[n] = raw_input('')
        P[n] = P[n].split()
        # print P[n]
        # print len(P[n]) is M
        C = len(P[n])
        if C == M:
            indx = 0
            for i in P[n]:
                i = ConvertToInt(i)
                CheckRange(i,1,1000)
                P[n][indx] =i
                indx = indx+1
                
        else:
            print "Invalid input, M:",M,"N: ",N,"len:",C
            exit()
    
    B = {}  
    for n in levels:
        
        line = fhandle.readline().strip()
        B[n] = line
        # B[n] = raw_input('')
        B[n] = B[n].split()
        if len(B[n]) == M:
            indx = 0
            for i in B[n]:
                i = ConvertToInt(i)
                CheckRange(i,1,1000)
                B[n][indx] =i
                indx = indx+1
              
        else:
            print "Invalid input, M:",M,"N: ",N
            exit()
        
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
        
        DPfromB = {}
        for kk in enemies:
            if DPfromB.has_key(B[i-1][kk]):
                # print DPfromB.get(B[i-1][kk])
                old_val = DPfromB.get(B[i-1][kk])
                DPfromB[B[i-1][kk]] = min(old_val,DP[i-1][kk])
            else:
                DPfromB[B[i-1][kk]] = DP[i-1][kk]
        fhand_write.write( "B[i-1]"+str( B[i-1])+"\n")
        B_sorted = B[i-1]
        B_sorted.sort()
        # fhand_write.write( "B[i-1]"+str( B[i-1])+"\n")
        fhand_write.write( "DPfromB"+str( DPfromB)+"\n")
        fhand_write.write( "B_sorted"+str( B_sorted)+"\n")
        DP_sorted = []
        for kk in B_sorted:
            DP_sorted.append(DPfromB[kk])
        fhand_write.write( "DP_sorted"+str( DP_sorted)+"\n")
        fhand_write.write( "P[i]"+str( P[i])+"\n")
        for j in enemies:
           
            match =next((x for x in B_sorted if x >= P[i][j]),None)
            # fhand_write.write( "match: "+str( match)+" ,P[i][j]:"+str(P[i][j])+"\n")
            if match is None:
                indx = len(B_sorted)
                min_1 = 100000
            else:
                indx = B_sorted.index(match)
                min_1 = min(DP_sorted[indx:len(DP_sorted)])
            # fhand_write.write( "indx: "+str(indx)+", min_1:"+str(min_1)+"\n")
            # print DP_sorted[indx:len(DP_sorted)]
            
            if indx > 0:
                rem = []
                for ii in range(0,indx):
                    rem.append(DP_sorted[ii]-B_sorted[ii])
                # fhand_write.write( "rem: "+str(rem)+"\n")
                min_2 = min(rem)
                # fhand_write.write( "min_1: "+str(min_1)+", min_2: "+str(min_2)+"\n")
                min_2 = min_2+P[i][j]
                # fhand_write.write( "min_2: "+str(min_2)+"\n")
                min_3 = min(min_1,min_2)
            else:
                min_3 = min_1
            # fhand_write.write( "min_3: "+str(min_3)+"\n")
            DP[i].append(min_3)
        # fhand_write.write( "DP: "+str(DP[i])+str(min(DP[i]))+"\n")    
            
    # fhand_write.write( str(min(DP[N-1]))+"\n")      
    fhand_write.write( str(min(DP[N]))+"\n")      
    # print (min(DP[N-1]))     
    print (min(DP[N]))       
    fhand_write.flush()
           
fhand_write.close() 
fhandle.close() 
ticks_2 =  time.time()
print "time: ",ticks_2-ticks_1