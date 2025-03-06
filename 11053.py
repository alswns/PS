import sys
from collections import deque
#브루트포스, 걍 떄려 박치기 하면 됨.
def input():
    return sys.stdin.readline().rstrip()

input()

datas=deque(map(int,input().split()))
dp=[0]*(max(datas)+1)
# st=datas.popleft()
# for i in range(st+1):
#     dp[i]=1
for data in datas:
    max_long =0
    for i in range(data):
        max_long=max(dp[i],max_long)
    dp[data] = max_long+1

print(max(dp))
