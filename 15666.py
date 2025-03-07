import itertools
n,m=map(int,input().split())

data=sorted(list(map(int,input().split())))
a=sorted(set(itertools.combinations_with_replacement(data,m)))
for i in a:
    for j in i:
        print(j,end=" ")
    print()
# print(a)

   1
  6 4
 3 7 2
5  