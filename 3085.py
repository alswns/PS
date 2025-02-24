import sys
read=sys.stdin.readline
n=int(read())
#색은 빨C 파P 초Z 노Y

c_count=0
p_count=0
z__count=0
y_count=0
red,blue,green,yellow='C','P','Z','Y'
board=[[] for i in range(n)]

for i in range(n):
    line=read().rstrip('\n')
    for j in line:
        board[i].append(j)

#가로 세기
for i in board:
    i.count()        
print(board)