import itertools 


m,n=map(int,input().split())
# help(itertools.combinations)
com=list(itertools.combinations_with_replacement(range(1,m+1),n))
# com=list(set(itertools.product(range(1,m+1),repeat=n)))
# help(com)

for i in com:
    for j in i:
        print(j,end=" ")
    print()