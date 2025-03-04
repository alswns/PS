import sys
import math
def input():
    return sys.stdin.readline().rstrip()

n=int(input())

dp=[sys.maxsize]*(n+1)
dp[0]=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if j*j>i:
            break
        dp[i]=min(dp[i],dp[i-j*j]+1)
print(dp[n])


