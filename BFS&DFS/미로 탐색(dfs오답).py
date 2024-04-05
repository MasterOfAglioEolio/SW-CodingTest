# 최단거리
# 1 이동 가능 0 이동 불가
# 1,1 출발

n,m=map(int,input().split())
maps=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    maps[i][1:]=list(map(int,input()))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
count=1
print(maps)
def dfs(x,y):
    global count
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<1 or ny<1 or nx>n or ny>m:
            continue
        if maps[nx][ny]==1:
            count += 1
            maps[nx][ny]=min(maps[x][y]+1,count)
            x=nx
            y=ny
            dfs(x,y)
    return maps[n][m]


maps[1][1]=2
print(dfs(1,1)-1)
for i in range(1,n+1):
    print(maps[i])
