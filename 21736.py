import sys
from collections import deque
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

n,m= map(int,input().split())
dataMap=[list(input()) for _ in range(n)]
v=[[False]*m for _ in range(n)]

x=0
y=0
ans=0
for dy in range(n):
    for dx in range(m):
        if dataMap[dy][dx]=="I":
            x=dx
            y=dy

def bfs(x,y):            
    q=deque()
    q.append([x,y])
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    v=[[False]*m for _ in range(n)]
    v[y][x]=True
    while q:
        qoo=q.popleft()
        for i in range(4):
            f_x=qoo[0]+dx[i]
            f_y=qoo[1]+dy[i]

            if f_x<0 or f_y<0 or f_y>= len(dataMap) or f_x>= len(dataMap[0]):
                continue
            if v[f_y][f_x]:continue
            if dataMap[f_y][f_x]=="X":continue
            if dataMap[f_y][f_x]=="P":
                global ans
                ans+=1
                
            v[f_y][f_x]=True
            q.append([f_x,f_y])
        
def dfs(x,y):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    global ans,dataMap
    
    for i in range(4):
        f_x=x+dx[i]
        f_y=y+dy[i]

        if f_x<0 or f_y<0 or f_y>= len(dataMap) or f_x>= len(dataMap[0]):
            continue
        if v[f_y][f_x]:
            continue
        if dataMap[f_y][f_x]=="P":
            ans+=1
            
        if dataMap[f_y][f_x]!="X":
                dataMap[f_y][f_x]="X"
                v[f_y][f_x]=True
                dfs(f_x,f_y)
                

        # if dataMap[f_y][f_x]=="O":
        #     if not check[f_y][f_x]:
        #         check[f_y][f_x]=True
        #         bfs(f_x,f_y)
        #         check[f_y][f_x]=False

        # elif dataMap[f_y][f_x]=="P":
        #     if not check[f_y][f_x]:
        #         n+=1
        #         dataMap[f_y][f_x]="O"
        #         check[f_y][f_x]=True
        #         bfs(f_x,f_y)
        #         check[f_y][f_x]=False
                
dfs(x,y)
if ans==0:
    print("TT")
else:
    print(ans)

