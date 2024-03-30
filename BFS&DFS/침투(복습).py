# 전류가 잘 흐르면 0 안 흐르면 1
# 마지막 행 까지 전달되면 성공 !
import sys
sys.setrecursionlimit(10**6)
m,n = map(int,input().split())

maps=[list(map(int,input())) for _ in range(m)]
visited=[[False]*n for _ in range(m)]


dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y):
    visited[x][y]=True

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or ny<0 or nx>=m or ny>=n:
            continue
        elif maps[nx][ny]==1:
            continue
        elif maps[nx][ny]==0 and visited[nx][ny]==False:
            dfs(nx,ny)



def solution(maps):
    for i in range(n):
        if maps[0][i]==0 and visited[0][i]==False:
            dfs(0,i)


    if True in visited[m-1]:
        print('YES')
    else:
        print('NO')



solution(maps)