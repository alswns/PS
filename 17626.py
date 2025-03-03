import sys
import math
def input():
    return sys.stdin.readline().rstrip()

n=int(input())


dp=[0]*(n+1)


    

dp[0]=0
# dp[1]=1
for i in range(1,n+1):
    min_data=sys.maxsize
    for j in range(1,50000):
        if j*j>i:
            break
        else : min_data=min(dp[i-j*j]+1,min_data)
    dp[i]=min_data   
    
print(dp[n])


