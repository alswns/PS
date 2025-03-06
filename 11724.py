import sys

def input():
    return sys.stdin.readline().rstrip()

n,m= map(int,input().split())

link_list=[[] for i in range(n+1)]

for _ in range(m):
    s,e=map(int,input().split())
    link_list[s].append(e)


for i in range(1,n+1):
    bfs


def bfs(start,link_list):

    return True

print(link_list)
