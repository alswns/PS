import sys
read=sys.stdin.readline
n=int(read())
    
N=1000001
num_list=[0] * (N+1)
f=[1]
for i in range(1,N):
    for j in range(1,N//2+1):
        if(i*j>=N):break
        num_list[i*j]=num_list[i*j]+ i

for i in range(2,N):
    f.append(f[-1]+num_list[i])

for i in range(n):
    s=int(read())
    print(f[s-1])
