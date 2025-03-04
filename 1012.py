import sys
sys.setrecursionlimit(10**5)
def input():
    return sys.stdin.readline().rstrip()

def dfs(dataList,x,y):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    dataList[y][x]=0

    for idx in range(4):
        f_x=x+dx[idx]
        f_y=y+dy[idx]

        if f_x<0 or f_y<0 or f_y>= len(dataList) or f_x>= len(dataList[0]):
            continue
        
        elif dataList[f_y][f_x]==1:
            dataList[f_y][f_x]=0
            dfs(dataList,f_x,f_y)
            
T=int(input())

for _ in range(T):
    m,n,k = map(int,input().split())

    dataList=[[0 for __ in range(m)] for __ in range(n)]
    
    for __ in range(k):
        x,y=map(int,input().split())

        dataList[y][x]=1
    count=0

    for x in range(m):
        for y in range(n):
            if dataList[y][x]==1:
                count+=1
                dfs(dataList,x,y)
    print(count)


    # print(dataList)