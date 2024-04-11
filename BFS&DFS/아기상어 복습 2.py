from collections import deque
n= int(input())

maps=[list(map(int,input().split())) for _ in range(n)]

#처음 사이즈 2
size=2

# 상좌하우
dx=[-1,0,1,0]
dy=[0,-1,0,1]

for i in range(n):
    for j in range(n):
        if maps[i][j]==9:
            sx,sy=i,j
            maps[i][j]=0


def bfs(x,y):
    # target 지정마다 visited 초기화
    visited = [[0] * n for _ in range(n)]

    # 시작점 방문처리
    visited[x][y]=1

    # target 리스트 초기화
    cand=[]
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                # 자신의 크기와 같은 물고기는 먹을 수 없다. / 하지만 지나갈 수 있다.
                if maps[nx][ny]==size or maps[nx][ny]==0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                # 자신의 크기보다 작은 물고기만 먹을 수 있다.
                elif 0< maps[nx][ny] < size:
                    visited[nx][ny]=visited[x][y]+1
                    queue.append((nx,ny))
                    cand.append((visited[nx][ny]-1,nx,ny))
                elif maps[nx][ny]>size:
                    continue

    # 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야 하는 칸의 개수의 최솟값이다.
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    # 정렬 우선순위 가까운 거리, x 좌표, y 좌표  ★이게 핵심인듯★
    return sorted(cand, key=lambda x:(x[0],x[1],x[2]))


cand=[]
size_count=0
time_sum=0
while True:

    # bfs의 결과 (제일 우선순위 target 으로 지정)
    cand=deque(bfs(sx,sy))
    print(cand)
    # target 없는 경우 break
    if not cand:
        break

    # 제일 우선순위까지 걸리는 시간 target x,y
    time,target_x,target_y=cand.popleft()
    time_sum+=time
    size_count+=1


    if size_count==size:
        size+=1
        size_count=0

    # target 먹음 처리 -> 0 으로
    maps[sx][sy]=0

    # target의 위치에서 시작

    sx, sy = target_x, target_y






print(time_sum)