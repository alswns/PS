import sys

def input():
    return sys.stdin.readline().rstrip()

n=input()

datas=list(map(int,input().split()))
new_data=sorted(list(set(datas)))

# ans=""
# O(n^2)
# for data in datas:
#     ans+=str(new_data.index(data))
#     ans+=" "

# print(ans[0:-1])

dict_data={}
for i in range(len(new_data)):
    dict_data[new_data[i]]=i

for data in datas:
    print(dict_data[data],end=" ")