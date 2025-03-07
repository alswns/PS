import math
from collections import deque
n=int(input())

# tree=[0]*(2**(int(math.log2(n))+1)+1)
# tree[1]=1

# class Node:
#     def __init__(self,node=None,value=0):
#         self.parentNode=node
#         self.value=value
        
#     def printNode(self):
#         print(self.parentNode.value)



nodeDict=[[]for i in range(n+1)]

for i in range(n-1):

    s,e=map(int,input().split())

    nodeDict[s].append(e)
    nodeDict[e].append(s)


ans=[0]*(n+1)

def bfs():
    v=[False]*(n+1)
    will=deque()
    will.append(1)

    while will:
        going=will.popleft()
            
        for item in nodeDict[going]:
            if v[item]:
                continue
            ans[item]=going

            # if target == item:
            #     print(going)
            #     return
            will.append(item)
            v[item]=True


#기존 방식은 for문 돌릴때마다 bfs호출해서 N배 거 시간이 걸림 그런데 어차피 다 출력 할거니깐 메모리 더 써서 저장하는게 맞음.
bfs()
for i in range(2,len(ans)):
    
    print(ans[i])
    

    

# nodeDict={}
# parent=Node(value=1)
# nodeDict[1]=parent

# after=deque()
# for i in range(n-1):

#     s,e=map(int,input().split())

#     after.append([s,e])

# while after:
#     s,e=after.popleft()
#     if s in nodeDict.keys():
#         nodeDict[e]=Node(nodeDict[s],e)    
#     elif e in nodeDict.keys():
#         nodeDict[s]=Node(nodeDict[e],s)    
#     else:
#         after.append([s,e])


# for i in range(2,n+1):
#     if i in nodeDict.keys():
#         nodeDict[i].printNode()