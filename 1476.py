import sys
read=sys.stdin.readline
E,S,M=1,1,1
E_max=15
S_max=28
M_max=19

max=7980

years=[[] for i in range(max+1)]

for i in range(1,max+1):
    years[i]=[E,S,M]
    E=E+1
    S=S+1
    M=M+1

    if E>E_max:
        E=1
    if S>S_max:
        S=1
    if M>M_max:
        M=1

input_E,input_S,input_M=map(int,read().rstrip('\n').split())

idx=years.index([input_E,input_S,input_M])
print(idx)