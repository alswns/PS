from collections import deque
n=int(input())

datas=deque()
input_list=[]

print_str=""
for _ in range(n):
    datas.append(int(input()))

can=True
for i in range(1,n+1):
    while datas[0] in input_list:
        while datas[0] in input_list:
            print_str+="-\n"
            input_list.pop()
        datas.popleft()
    
    print_str+="+\n"
    input_list.append(i)
    

if list(datas) == input_list[::-1]:
    print(print_str.rstrip())
    for data in datas:
        print("-")
else:
    print("NO")
    
        

