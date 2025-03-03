import sys
def input():
    return sys.stdin.readline().rstrip()

n,k=map(int,input().split())

datalist=[]

for _ in range(n):
    datalist.append(int(input()))


count=0

for data_idx in range(len(datalist)-1,-1,-1):
    if datalist[data_idx]<=k:
        max_big_idx=data_idx
        break

while k>0:
    max_data=datalist[max_big_idx]
    if k>=max_data:
        k-=max_data
        count+=1
    else:max_big_idx-=1
    
print(count)