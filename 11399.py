import sys
def input():
    return sys.stdin.readline().rstrip()

n=int(input())


data=list(map(int,input().split(" ")))
data.sort()

time=0
for i in range(len(data)):
    time+=(data[i]*(len(data)-i))

print(time)