import sys
n=int(sys.stdin.readline().rstrip())

data_set=set()
a=set()
for i in range(1,21):
    a.add(i)

for _ in range(n):
    data=sys.stdin.readline().rstrip().split(" ")
    
    if len(data)>1:
        status=data[0]
        count=int(data[1])

        if status=="add":
            data_set.add(count)
            
        elif status=="remove":
            data_set.discard(count)
        elif status=="check":
            print("1" if count in data_set else "0")
        elif status=="toggle":
            if count in data_set:
                data_set.remove(count)
            else:
                data_set.add(count)
    else:
        status=data[0]

        if status=="all":
            data_set=a
        elif status=="empty":
            data_set.clear()