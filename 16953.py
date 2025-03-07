import sys
from collections import deque
# down Top방식으로 했어는데 그러니깐 너무 메모리 낭비가 심하다. 이럴땐 TOP DOWN방식이 더 효율 적인듯 메모리도 덜 쓰고 계산도 적게하니깐
def input():
    return sys.stdin.readline().rstrip()

s,e=map(int,input().split())

# def ans():
#     q=deque()
#     q.append(s)
#     n=0
#     while q:
#         if min(q)>e:
#             return -1
        
#         for i in range(len(q)):
#             d=q.popleft()

            
#             if d==e:
#                 return n
            
#             q.append(d*10+1)
#             q.append(d*2)

#         n+=1


def ans():
    q=deque()
    q.append(e)
    n=0
    
    #e의 뒤가 1로 끝나면 1때고 2로 나눠지면 2로 나눔
    while q:
        
        # if max(q)<s:
        #     return -1
        
        for i in range(len(q)):
            d=q.popleft()
            

            if d==s:
                return n
            
            if d%10 == 1:
                t=d//10
                if t>=s:
                    q.append(d//10)
            elif d%2==0:
                t=d//2
                if t>=s:
                    q.append(d//2)

        n+=1
    return -1

a=ans()

if a==-1:
    print(-1)
else:
    print(a+1)