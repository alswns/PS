import math
n=int(input())

logn=math.log2(n)

if  logn==int(logn):
    print(n)
else:
    print(2*(n - 2**int(logn)))

def fun(n):
    # print("%d 시작!!!!!!"%(n))
    if n==1:return 
    deck=[i for i in range(1,n+1)]
    # print("log2(%d) : %d"%(n,math.log2(n)),end='\t')
    while True:
        # print(deck)
        deck=deck[1:]
        if len(deck)<=1: break
        a=deck[0]
        deck=deck[1:]
        deck.append(a)
        # print(deck)

        
    print("%d : %d  "%(n,deck[0]),end=' ')

    logn=math.log2(n)

    if  logn==int(logn):
        print(n)
    else:
        print(2*(n - 2**int(logn)))

# for i in range(1,1000,1):
#     fun(i)
    



