# 어떤 배추에 배추흰지렁이가 한마리라도 살고있으면 이지렁이는 다른 배추로 이동 가능
# 그 배추들은 해충으로부터 보호받을 수 있음
# 상하좌우 네 방향에 다른 배추가 위치한 경우 서로 인접한 경우임

# 배추들이 모여있는 곳에는 배추지렁이 한마리만 있으면 됨
# 총 몇마리 지렁이가 필요한가 ? (군집) (dfs or bfs)
import sys
sys.setrecursionlimit(10**6)
dx=[-1,0,1,0]
dy=[0,1,0,-1]




t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    maps = [[0] * m for _ in range(n)]
    visited=[[False]*m for _ in range(n)]
    for _ in range(k):
        y,x=map(int,input().split())
        # print(x,y)
        maps[x][y]=1

    count=0
    def dfs(x, y):
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # print(nx,ny)
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if maps[nx][ny]==1 and visited[nx][ny]==False:
                visited[nx][ny]=True
                dfs(nx,ny)

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and visited[i][j]==False:
                count+=1
                dfs(i,j)

    print(count)



    # for i in range(n):
    #     print(maps[i])


