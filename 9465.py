import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

t=int(input())

for _ in range(t):
    #0 : up, # 1 : down, 2 : no
    n=int(input())
    dataList=[]
    dp=[[0]*n for i in range(3)]

    for i in range(2):
        dataList.append(list(map(int,input().split())))

    dp[0][0]=dataList[0][0]
    dp[1][0]=dataList[1][0]

    for i in range(1,len(dataList[0])):
        
        dp[0][i]=dataList[0][i]+ max(dp[1][i-1],dp[2][i-1])

        dp[1][i]=dataList[1][i]+ max(dp[0][i-1],dp[2][i-1])

        dp[2][i]=max(dp[0][i-1],dp[1][i-1],dp[2][i-1])
        

    ans = max(dp[0][-1],dp[1][-1],dp[2][-1])
    print(ans)

    
