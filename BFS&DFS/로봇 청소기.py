# 로봇 청소기가 방의 청소하는 영역의 개수를 구해라 !
# 1) 현재 칸이 청소되지 않은 경우 현재 칸을 청소한다.
# 2) 현재 칸의 주변 4칸 중 모두 청소된 경우
#    2-1) 바라보는 방향을 유지한 채 한 칸 후진할 수 있다면 한 칸 후진한 후 1번으로 돌아간다 (turn) O
#    2-2) 바라보는 방향의 뒤쪽 칸이 벽이라 후진 불가능하면 break O
# 3) 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
#    3-1) 반시계 방향으로 90도 회전
#    3-2) 바라보는 방향 기준으로 앞쪽칸이 청소되지 않은 경우 한칸 전진
# 0 : 청소되지 않은 상태 1 : 벽이 있는 것
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
r,c,d=map(int,input().split())

dx=[-1,0,1,0]
dy=[0,1,0,-1]

maps=[]
visited=[[False]*m for _ in range(n)]

for i in range(n):
    maps.append(list(map(int,input().split())))

count=0
def turn(direction):
    if direction==0:
        direction=3
    else:
        direction-=1
    return direction
def dfs(x,y,d):
    global count
    turn_count=0

    if visited[x][y] == False:
        visited[x][y]=True
        count+=1

    for i in range(4):
        nd=(d+3)%4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if maps[nx][ny]==0 and visited[nx][ny]==False:
            dfs(nx,ny,nd)
            return
        d=nd
        turn_count+=1

    if turn_count==4:
        nx=x-dx[d]
        ny=y-dy[d]
        if maps[nx][ny]==1:
            return
        dfs(nx,ny,d)

dfs(r,c,d)

print(count)