n=int(input())
maps=[[0]*n for _ in range(n)]
visited=[[False]*n for _ in range(n)]
for i in range(n):
    maps[i]=list(map(int,input()))

#단지수 총 출력 및 각 단지에 속하는 집의 수를 오름차순으로 정렬

dx=[-1,0,1,0]
dy=[0,1,0,-1]

from collections import deque
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    count=1
    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if maps[nx][ny]==1 and visited[nx][ny]==False:
                visited[nx][ny]=True
                queue.append((nx,ny))
                count+=1
    return count

answer=[]
for i in range(n):
    for j in range(n):
        if maps[i][j]==1 and visited[i][j]==False:
            visited[i][j]=True
            answer.append(bfs(i,j))
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])
