import itertools
n,m=map(int,input().split())

data=set(map(int,input().split()))
a=sorted(list(itertools.permutations(data,m)))

for i in a:
    for j in i:
        print(j,end=" ")
    print()
# print(a)

