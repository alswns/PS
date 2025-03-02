from collections import deque

n,k=map(int,input().split())

queue=deque(i for i in range(1,n+1))
print("<",end='')

while(True):
    if len(queue)<=1:
        print("%d>"%queue[0])
        break
    for i in range(1,k+1):
        
        temp=queue.popleft()
        if i == k:
            print("%d, "%(temp),end="")
        else:
            queue.append(temp)

    
