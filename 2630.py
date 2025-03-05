import sys

def input():
    return sys.stdin.readline().rstrip()

n= int(input())

dataMap=[]

ans=[0,0]
def isFull(dataMap):
    if len(dataMap)<=1:
        return True
    init=dataMap[0][0]
    for i in range(len(dataMap[0])):
        for j in range(len(dataMap)):
            if dataMap[i][j]!=init:
                return False
            
    return True

for _ in range(n):
    data=list(map(int,input().split()))
    dataMap.append(data)
    
splitDataMap=[dataMap]

while True:
    
    if len(splitDataMap)<=0:break
    replaceMap=[]
    

    for data in splitDataMap:
        if isFull(data):
            ans[data[0][0]]+=1
            break
        #4
        maps = [[],[],[],[]]
        
        for i in range(len(data)):
            if i<len(data)/2:
                maps[0].append(data[i][0:len(data)//2])
                maps[1].append(data[i][len(data)//2:])
            else:
                maps[2].append(data[i][0:len(data)//2])
                maps[3].append(data[i][len(data)//2:])
    
        for val in maps:
            if isFull(val):
                ans[val[0][0]]+=1
            else:
                replaceMap.append(val)
    splitDataMap=replaceMap

for a in ans:
    print(a)
    
    
    