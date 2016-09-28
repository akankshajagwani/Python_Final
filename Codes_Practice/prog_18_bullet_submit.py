# https://www.hackerrank.com/challenges/a-super-hero
#consider having a gui tktinker



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

    P = {}    
    for n in range(1,N+1):
        line = fhandle.readline().strip()
        P[n] = line
        # P[n] = raw_input('')
        P[n] = P[n].split()
        if len(P[n]) is M:
            indx = 0
            for i in P[n]:
                i = ConvertToInt(i)
                CheckRange(i,1,1000)
                P[n][indx] =i
                indx = indx+1
        else:
            print "Invalid input"
            exit()
    B = {}  
    
    for n in range(1,N+1):
        B_P[n] = {}
        line = fhandle.readline().strip()
        B[n] = line
        # B[n] = raw_input('')
        B[n] = B[n].split()
        if len(B[n]) is M:
            indx = 0
            for i in B[n]:
                i = ConvertToInt(i)
                CheckRange(i,1,1000)
                B[n][indx] =i
                if B_P[n].has_key(P[n][indx]) is False:
                B_P[n][P[n][indx]] = i
                else:
                    lst = B_P[n].get(P[n][indx])
                    lst.append(i)
                    B_P[n][P[n][indx]] = lst
                    
                indx = indx+1
        else:
            print "Invalid input"
            exit()
        fhand_write.write(str(P[n])+'\n') 
        fhand_write.write(str(B[n])+'\n') 
    # fhand_write.write(str(P[1])+'\n') 
    # fhand_write.write(str(B[1])+'\n') 
    # fhand_write.write(str(P[2])+'\n') 
    lst_minBullet = []
    for minPower in P[1]:
        print "minPower:",minPower
        MinBullet = 0
        MinBullet = MinBullet + minPower
        indxs = (i for i,value in enumerate(P[1]) if value == minPower)
        bullets = []
        for indx in indxs: 
            bullets.append(B[1][indx])
        BulletAdded = max(bullets)
        
        levels = range(2,N+1)
        BulletAdded_old = BulletAdded
        for n in levels:
            print "n:",n
            
            ii = 0
            p1 = []
            b1 = []
            for p in P[n]:
                if p < BulletAdded:
                    p1.append(p)
                    b1.append(B[n][ii])
                ii = ii+1
            print "p1:",p1
            print "b1:",b1
            if len(b1) < 1:
                minPower = min(P[n])
                indxs = (i for i,value in enumerate(P[n]) if value == minPower)
                bullets = []
                for indx in indxs: 
                    bullets.append(B[n][indx])
                BulletAdded = max(bullets)
            else:   
                BulletAdded = max(b1)
                print "BulletAdded", BulletAdded
                indx = b1.index(BulletAdded)
                minPower = p1[indx]
                print "minPower:",minPower
            
            balance = BulletAdded_old - minPower
            print "balance:",balance,"BulletAdded_old",BulletAdded_old,"minPower:",minPower
            BulletAdded_old = BulletAdded
            if balance < 0:
                MinBullet = MinBullet + abs(balance)
          
            print "MinBullet:",MinBullet,"n:",n
        lst_minBullet.append(MinBullet)
    print "lst_minBullet:",lst_minBullet
    MinBullets.append(min(lst_minBullet))
    
for t in range(1,T+1):
    fhand_write.write(str(MinBullets[t-1])+'\n') 
    # print MinBullets[t-1]
    
fhand_write.close() 
fhandle.close() 