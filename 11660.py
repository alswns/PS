import sys
def input():
    return sys.stdin.readline().rstrip()

n,m=map(int,input().split())


dataMap=[
    list(map(int,input().split()))
      for i in range(n)]
dp=[[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if j==0:
            dp[i][j]=dataMap[i][j]
        else:
            dp[i][j]=dp[i][j-1]+dataMap[i][j]




# print(dataMap)

# print(dp)

for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    x1-=1
    x2-=1
    y1-=1
    y2-=1
    ans=0
    
    for i in range(x1,x2+1):
        # print(da)
        if y1==0:
            # dp[y][x]
            ans+= dp[i][y2]
        else:
            ans+= dp[i][y2]-dp[i][y1-1]
        # print(y1,y1,x2,y2)
        # if x1==0:
            # dp[y][x]
        #     ans+= dp[x2][i]
        # else:
        #     ans+= dp[x2][i]-dp[x1-1][i]

        # print(ans)
    print(ans)

