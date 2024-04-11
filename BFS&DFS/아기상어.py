from collections import deque
#아기 상어, 물고기 모두 크기를 가지고 있음 (자연수)
# 1) 가장 처음 아기상어 크기 : 2
# 2) 아기상어는 1초에 상하좌우로 인접한 한칸씩 이동
# 3) 아기상어는 자신의 크기보다 큰 물고기가 있는 칸은 지날 수 없음 (벽)
# 4) 아기상어는 자신의 크기보다 작은 물고기만 먹을 수 있음
# 5) 아기상어는 자신의 크기와 같은 물고기는 먹을 수 없으나 그 물고기가 있는 칸은 지날 수 있음


# 이동 방법
# 1) 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기상어는 엄마상어에게 도움을 요청함
# 2) 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 감
# 3) 먹을 수 있는 물고기가 1마리보다 많다면 거리가 가장 가까운 물고기를 먹으러 감
# 3-2) 거리는 아기상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값
# 3-3) 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 많다면 > 왼쪽에 있는 물고기

# 크기 증가
# 1) 아기상어는 자신의 크기와 같은 수의 물고기를 먹을 떄 마다 크기가 1 증가한다.

# 공간의 상태가 주어졌을 떄 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아 먹을 수 있는지 프로그램을 작성


n= int(input())

# 0 빈칸
# 1,2,3,4,5,6 물고기의 크기
# 9 아기상어의 위치

# maps 초기화
maps=[[0]*(n) for _ in range(n)]
# shark_maps 초기화
shark_mpas=[[0]*(n) for _ in range(n)]

# maps 데이터 입력
for i in range(n):
    maps[i]=list(map(int,input().split()))
print(maps)

# 처음 아기상어 사이즈 2 초기화
size=2
# 시작 좌표 초기화
sx,sy=0,0

# 마지막 하나 남았을 경우 target 좌표
target_x=0
target_y=0
def check():
    count=0
    global sx,sy,target_x,target_y
    for i in range(n):
        for j in range(n):
            if maps[i][j] in (1,2,3,4,5,6):
                count+=1
                # count가 1일 경우 미리 저장
                target_x=i
                target_y=j
            if maps[i][j]==9:
                sx=i
                sy=j
                shark_mpas[sx][sy]=size
    if count==0:
        return 0
    if count==1:
        return 1
    return 2

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(sx,sy):
    eat_count=0
    # 시간 초기화
    time=0

    global size

    queue= deque()
    queue.append((sx,sy))
    print(sx,sy)
    while queue:
        x,y=queue.popleft()
        print(x,y)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if maps[nx][ny]>size and maps[nx][ny]!=0:
                continue
            if maps[nx][ny]<size and maps[nx][ny]!=0:
                maps[nx][ny]=0
                eat_count+=1
                # size +1
                if eat_count==size:
                    eat_count=0
                    size +=1
            # 이외에 사이즈가 같은 경우 아무 일도 없음

            time+=1
            shark_mpas[x][y]=0
            shark_mpas[nx][ny]=size
            queue.append((nx,ny))
    return maps[target_x][target_y]
        # print("-------------")
        # for i in range(n):
        #     print(shark_mpas[i])


def solution():
    time=0
    if check()==0:
        return time
    elif check()==1:
        bfs(sx,sy)
        return time
    elif check()==2:
        bfs(sx,sy)
        return time





print(solution())
print(maps)
print("------")
print(shark_mpas)
# 3
# 0 0 0
# 0 0 0
# 0 9 0