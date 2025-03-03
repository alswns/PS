import sys
def input():
    return sys.stdin.readline().rstrip()

n=int(input())


for _ in range(n):
    cloth_dict=dict()
    m=int(input())

    for i in range(m):
        cloth,cate=input().split(" ")

        if cate in cloth_dict.keys():
            cloth_dict[cate]=cloth_dict[cate]+1
        else : 
            cloth_dict[cate]=2
    ans=1
    for data in cloth_dict.values():
        ans*=data
    ans-=1
    print(ans)
