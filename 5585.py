n=1000-int(input())


en=[500,100,50,10,5,1]

idx=0
ans=0

while idx<6:
    if en[idx]>n:
        idx+=1
    else:
        n-=en[idx]
        ans+=1

print(ans)