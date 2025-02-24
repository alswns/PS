import sys
N=1000000

MAX=int(N**(1/2))+1
isPrime=[True]*(N+1)
isPrime[0],isPrime[1]=False,False
for i in range(2,MAX):
    for j in range(2,N//i+1):
        isPrime[i*j]=False


while True:
    ls=[]
    n=int(sys.stdin.readline())
    if n==0:break

    printed=False
    for i in range(3, n//2+1):
        if isPrime[i] and isPrime[n-i]:
            print("%d = %d + %d"%(n,i,n-i))
            printed=True
            break
        
    if not printed:print("Goldbach's conjecture is wrong.")
            
        