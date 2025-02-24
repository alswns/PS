import sys 
read=sys.stdin.readline
channels=[str(i) for i in range(2000000)]

target = int(read())
n=int(read())
dont_button=read().strip('\n').split()

def filt(data,t):
    if data.find(t)==-1:
        return True
    return False

for i in dont_button:
    channels=[channel for channel in channels if filt(channel,i)]

dif= abs(target-100)

for i in channels:
    try:
        c_dif=abs(target-int(i))+len(i)
        dif = dif if dif<c_dif else c_dif
    except Exception:
        break

    
print(dif)


