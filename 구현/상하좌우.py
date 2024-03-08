n=int(input())
m=input().split()

x,y=1,1

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']


for move in m: # 이동계획 하나씩 확인하기
    for i in range(len(move_types)):
        if move == move_types[i]: # 이동 후 좌표 구하기
            nx=x+dx[i]
            ny=y+dy[i]

    if nx<1 or ny<1 or nx>n or ny>n: # 공간을 벗어나는 경우 (1,1) ~ (n,n) 무시
        continue
    x,y=nx,ny # 이동 수행

print(x,y)
# 5
# R R R U D D