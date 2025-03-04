import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

data=input()

datas=deque()

start_idx=0
for idx in range(len(data)):
    if data[idx]== "+" or data[idx]== "-" :
        datas.append(data[start_idx:idx])
        datas.append(data[idx])
        start_idx=idx+1
datas.append(data[start_idx:])

ans=0
cach=0
parentheses=False
for data in datas:
    if data.isnumeric():
        if parentheses:
            ans-=int(data)
        else:
            ans+=int(data)
    else:
        if data=="-":
            parentheses=True
        
        
print(ans)