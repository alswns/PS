N=10001

isPrime=[True]*N

for i in range(2,N):
    for j in range(2,N//i+1):
        x=i*j
        if x>=N:break
        isPrime[x]=False

x,y=map(int,input().split())

common=1
for i in range(2,min(x,y)+1):
    if x%i==0 and y%i==0:
        common=i
print(common)
print(x*y//common)
    