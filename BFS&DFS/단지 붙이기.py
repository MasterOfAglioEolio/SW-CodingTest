# 1 집있는 곳  0 집 없는 곳
# 단지수 출력, 각 단지에 속하는 집 오름차순으로 정렬
# dfs

n= int(input())
maps=[[0]*(n) for _ in range(n)]
visited=[[False]*(n) for _ in range(n)]

for i in range(n):
    maps[i]=list(map(int,input()))

count=0 # 단지 수 구분
answer=[]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(x,y):
    result=1 # 원소의 개수 세기
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        # 인접한 위치가 범위를 벗어나는 경우 무시
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        if maps[nx][ny]==1:
            maps[nx][ny]=-1
            result+=dfs(nx,ny)
    return result

for i in range(n):
    for j in range(n):
        if maps[i][j]==1:
            maps[i][j]=-1
            answer.append(dfs(i,j))

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])
