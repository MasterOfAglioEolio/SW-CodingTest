
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도) 부터 차례대로 갈 곳을 정한다
# 2. 캐릭터의 왼쪽 방향에 가지 않은 곳 있다면 왼쪽 방향으로 회전 후 왼쪽으로 한 칸 전진
# 3. 왼쪽에 가보지 않은 칸이 없다면 왼쪽으로 회전 수행 후 다시 1단계
# 4. 네 방향 모두 가본 칸이거나 바다일 경우, 바라보는 방향 유지한 채 한칸 뒤로 가고 1단계로
# 5. 뒤쪽 방향이 바다일 경우 움직임을 멈춘다.

n,m=map(int,input().split())
d=[[0]*m for _ in range(n)]
x,y,direction=map(int,input().split())

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

d[x][y]=1
count=1
turn_count=0
# 북 동 남 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global direction
    direction-=1
    if direction==-1: # 반시계 방향으로 회전
        direction=3

while True:
    #왼쪽으로 호전
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    if nx<0 or ny<0 or nx>n or ny>m: # 맵을 벗어나는 경우
        continue
    # 가보지않은 칸이 존재하는 경우 + 육지인 경우
    elif d[nx][ny]==0 and array[nx][ny]==0:
        d[nx][ny]=1
        x, y = nx, ny
        count+=1
        turn_count=0
        continue
    # 회전한 이후 정면에 가보지않은 칸이 없거나 바다인 경우
    else:
        turn_count+=1
    # 네방향 모두 갈 수 없는 경우
    if turn_count==4:
        # 뒤로 가기
        nx=x-dx[direction]
        ny=y-dy[direction]
        if array[nx][ny]==0: # 뒤로 갈 수 있으면 뒤로
            x,y=nx,ny
        else:  # 뒤로 갔는데 바다인 경우
            break
        turn_count=0
print(count)




# 4 5
# 1 1 0
# 1 1 1 1 1
# 1 0 0 0 1
# 1 1 0 0 1
# 1 1 1 1 1