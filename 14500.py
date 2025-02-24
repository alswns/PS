n,m=map(int,input().split())  #n*m
gr=[]
for i in range(n):
    gr.append(list(map(int,input().split(' '))))

dx=[0,0,1,-1]
dy=[1,-1,0,0]


start_point=[]
for y in range(n):
    for x in range(m):
        start_point.append([y,x])


for y,x in start_point:
    point_x=x
    point_y=y

    hap=gr[point_x][point_y]
    for _ in range(3):    
        bigger=0
        for i in range(0,4):
            try:
                if hap[point_x+dx[i]][point_y+dy[i]]>bigger:
                    point_x=point_x+dx[i]
                    point_y=point_y+dy[i]
                    bigger=hap[x+dx[i]][y+dy[i]]
                
            except Exception:
                pass
        hap=hap+bigger
    print(hap)
        