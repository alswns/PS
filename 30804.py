import sys
from collections import deque
import copy
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()
n=int(input())
datas=deque(map(int,input().split()))

def getCount(datas):
    return len(deque(set(datas)))

for i in range(len(datas)):
    each_datas=copy.deepcopy(datas)
    if getCount(each_datas)<=2:
            break
    
    for j in range(0,len(datas)-i):
        if getCount(each_datas)<=2:
            break
        each_datas.popleft()

    if getCount(each_datas)<=2:
            break
    
    for j in range(len(datas)-i, len(datas)):
        if getCount(each_datas)<=2:
            break
        each_datas.pop()



    