from collections import deque
n=int(input())

del_num= int(n*(0.15)+0.5)



data=[]
for _ in range(n):
    data.append(int(input()))
data.sort()

data=deque(data)

for i in range(del_num):
    data.pop()
    data.popleft()
# print(data)
if len(data)==0:
    print(0)
else:
    answer=int(sum(data)/len(data)+0.5)
    print(answer)