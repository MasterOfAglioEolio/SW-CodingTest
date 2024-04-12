n=int(input())
maps=[[0]*n for _ in range(n)]
visited=[[False]*n for _ in range(n)]


for i in range(n):
    maps[i]=list(map(int,input()))

#단지수 총 출력 및 각 단지에 속하는 집의 수를 오름차순으로 정렬

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    count=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        if maps[nx][ny]==1 and visited[nx][ny]==False:
            visited[nx][ny]=True # 방문처리
            count+=dfs(nx,ny)
    print(count)
    return count

answer=[]
for i in range(n):
    for j in range(n):
        if maps[i][j]==1 and visited[i][j]==False:
            visited[i][j]=True
            answer.append(dfs(i,j))
print(answer)