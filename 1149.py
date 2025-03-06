import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n=int(input())

price=[]
for _ in range(n):
    data=list(map(int,input().split()))
    price.append(data)

dp=[[0,0,0] for _ in range(n)]

dp[0][0]=price[0][0]
dp[0][1]=price[0][1]
dp[0][2]=price[0][2]

#0 : R, 1 : G, 2 : B
for i in range(1,n):

    dp[i][0]=price[i][0]+min(dp[i-1][1],dp[i-1][2])

    dp[i][1]=price[i][1]+min(dp[i-1][0],dp[i-1][2])

    dp[i][2]=price[i][2]+min(dp[i-1][1],dp[i-1][0])

print(min(dp[-1]))

    # dp[i]=dp[i-2]