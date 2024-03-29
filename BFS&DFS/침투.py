from collections import deque

# 위쪽 : 바깥쪽   아래쪽 : 안쪽

n,m=map(int,input().split())

maps=[list(map(int,input())) for _ in range(n)]


print(n,m)

print(maps)

def bfs(x,y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            elif maps[nx][ny]==0:
                continue
            elif maps[nx][ny]==1:
                maps[nx][ny]=2
                queue.append((nx,ny))

    print(maps)
    # return maps[n-1][m-1]


def solution(maps):

    for i in range(m):
        bfs(0,i)

        # if answer >= n//2:
        #     return True
        # else:
        #     return False



print(solution(maps))