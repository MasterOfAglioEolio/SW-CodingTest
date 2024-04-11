from collections import deque

n = int(input())
maps = [[0] * (n) for _ in range(n)]
# maps 데이터 입력
for i in range(n):
    maps[i] = list(map(int, input().split()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            sx, sy = i, j
            maps[sx][sy] = 0  # 상어의 초기 위치를 지움

cnt = 0
size = 2
size_count = 0
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cand = []
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if maps[nx][ny] == 0 or maps[nx][ny] == size:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                elif 0 < maps[nx][ny] < size:
                    visited[nx][ny] = visited[x][y] + 1
                    cand.append((visited[nx][ny] - 1, nx, ny))

    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))

while True:
    cand = deque(bfs(sx, sy))

    if not cand:
        break

    time, target_x, target_y = cand.popleft()
    cnt+=time
    size_count+=1

    if size==size_count:
        size+=1
        size_count=0

    maps[sx][sy]=0
    sx,sy=target_x,target_y

print(cnt)
