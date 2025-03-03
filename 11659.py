

import sys
def input():
    return sys.stdin.readline().rstrip()

n,t=map(int,input().split())

datas=list(map(int,input().split()))


dp=[0]*(n+1)

dp[0]=0
dp[1]=datas[0]
for i in range(1,n):
    dp[i+1]=dp[i]+datas[i]

for i in range(t):
    s,e=map(int,input().split())
    # print(s,e)
    print(dp[e]-dp[s-1])
    