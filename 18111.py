import sys
import math
def input():
    return sys.stdin.readline().rstrip()

n,m,b = map(int,input().split())

dataMaps=[]

for _ in range(n):
    data=list(map(int,input().split()))
    dataMaps.append(data)

blocks=b
for data in dataMaps:
    blocks+=sum(data)

maxFloor=blocks//(n*m)
    
total_time=sys.maxsize
ans=0
for i in range(0,maxFloor+1):
    local_time=0
    for data in dataMaps:
        for x in data:
            minus=x-i
            if minus>0:
                local_time+=minus*2
            elif minus<0:
                local_time+=minus*(-1)
    if local_time<=total_time:
        total_time=local_time
        ans=i
print(f"{total_time} {ans}")