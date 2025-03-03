import sys
n=int(sys.stdin.readline().rstrip())

data_set=set()

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
                data_set.discard(count)
            else:
                data_set.add(count)
    else:
        status=data[0]

        if status=="all":
            data_set=set(list(range(1,21)))
        elif status=="empty":
            data_set=set()
