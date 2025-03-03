import sys
def read():
    return sys.stdin.readline().rstrip()
n,m=map(int,read().split())

pocketmon_dict=list()
for i in range(n):
    pocketmon_dict.append(read())

for i in range(m):
    data=read()
    if data.isnumeric():
        print(pocketmon_dict[int(data)-1])
    else:
        
        print(pocketmon_dict.index(data)+1)

