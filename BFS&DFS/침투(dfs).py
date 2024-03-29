from collections import deque

# 위쪽 : 바깥쪽   아래쪽 : 안쪽

n,m=map(int,input().split())

maps=[list(map(int,input())) for _ in range(n)]

visited=[[False]*m for _ in range(n)]

print(n,m)

print(maps)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x,y):
    visited[x][y]=True

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        elif maps[nx][ny]==1:
            continue
        elif maps[nx][ny]==0 and visited[nx][ny]==False:
            dfs(nx,ny)



def solution(maps):

    for i in range(m):
        if maps[0][i]==0 and visited[0][i]==False:
            dfs(0,i)
    print(visited)
    if True in visited[n-1]:
        print('YES')
    else:
        print('NO')



solution(maps)