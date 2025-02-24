N=1000000

MAX=int(N**(1/2))+1
isPrime=[True]*(N+1)
isPrime[0],isPrime[1]=False,False
for i in range(2,MAX):
    for j in range(2,N//i+1):
        
        isPrime[i*j]=False

x,y=map(int,input().split())

for i in range(x,y+1):
    if isPrime[i]:
        print(i)
    