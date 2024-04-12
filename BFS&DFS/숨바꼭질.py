n,k=map(int,input().split())
MAX=10**5
maps=[0]*(MAX+1)
from collections import deque

def bfs(n):

    queue=deque()
    queue.append(n)

    while queue:
        x=queue.popleft()

        if x == k:
            # print(maps[k])
            break
        for nx in (x-1,x+1,x*2):

            if 0<=nx<=MAX and not maps[nx]:
                maps[nx]=maps[x]+1
                queue.append(nx)

    return maps[k]

print(bfs(n))
