import sys
from collections import deque
import heapq

def input():
    return sys.stdin.readline().rstrip()

n= int(input())
heap_list = []

int_max=sys.maxsize
for _ in range(n):
    indata=int(input())
    if indata ==0:

        if len(heap_list)==0:
            print("0")
        else:
            print(int_max-heapq.heappop(heap_list))
    
    else:
       heapq.heappush(heap_list, int_max-indata)

            
        