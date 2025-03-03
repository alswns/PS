import sys
def input():
    return sys.stdin.readline().rstrip()

data_dict=dict()

n,m=map(int,input().split())

for _ in range(n):
    key,val=input().split(" ")
    data_dict[key]=val

for _ in range(m):
    print(data_dict[input()])