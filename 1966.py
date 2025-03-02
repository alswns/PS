from collections import deque
t=int(input())

for _ in range(t):
    n,m=map(int,input().split())

    impor = deque(map(int,input().split()))

    idx = m
    nth=1
    while True:
        temp=impor.popleft()


        if len(impor)==0:
            print(nth)
            break

        if temp >= max(impor):
            if idx == 0 : print(nth);break
            else: nth+=1;idx -= 1

        else:
            impor.append(temp)
            if idx == 0:
                idx += len(impor)-1
            else:
                idx-=1
        # print(max(impor))