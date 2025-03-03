import sys
def input():
    return sys.stdin.readline().rstrip()

n,m=map(int,input().split())

heard=set()
see=set()
for _ in range(n):
    heard.add(input())
for _ in range(m):
    see.add(input())

new_set=heard&see
ans_list=list(new_set)
ans_list.sort()

print(len(ans_list))

for val in ans_list:
    print(val)
