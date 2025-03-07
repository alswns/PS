import itertools
n,m=map(int,input().split())

data=list(map(int,input().split()))
a=sorted(set(itertools.permutations(data,m)))

for i in a:
    for j in i:
        print(j,end=" ")
    print()
# print(a)

