import sys

read=sys.stdin.readline
n,k = map(int,read().rstrip().split())

datas=[]

for _ in range(n):
    datas.append(int(read().rstrip()))



max_length=0             

st=1
lt=max(datas)

while lt>=st:
    mid=(lt+st)//2

    count=0
    for data in datas:
        count+=data//mid
    if count>=k:
        max_length=mid
        st=mid+1
    elif count<k:
        lt=mid-1

#이부분만 수정하면 될듯
   

    
print(max_length)