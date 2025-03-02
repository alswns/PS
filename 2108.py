from collections import Counter
n=int(input())

data=[]

for _ in range(n):
    data.append(int(input()))

data.sort()

if sum(data)<0:
    a= -sum(data)/len(data)
    print(-int(a+0.5))
else:
    print(int(sum(data)/len(data)+0.5))
print(data[int(len(data)/2)])


count=Counter(data)
ct=count.most_common()

if len(ct)==1:
    print(data[0])
else:
    if ct[0][1] == ct[1][1]:
        print(ct[1][0])
    else:
        print(ct[0][0])


if len(data)==1:
    print("0")
else:
    ran=max(data)-min(data)
    print(ran)


