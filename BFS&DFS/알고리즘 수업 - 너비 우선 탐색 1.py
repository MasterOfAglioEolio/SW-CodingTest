import sys
from collections import deque
sys.setrecursionlimit(150000)

n,m,r = map(int,sys.stdin.readline().split())

graph=[[] for i in range(n+1)]
visited=[0]*(n+1)
count=1

for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
def bfs(data):
    global count
    visited[data]=count
    queue=deque()
    queue.append(data)
    while queue:

        node=queue.popleft()
        graph[node].sort(reverse=True)
        for i in graph[node]:
            if visited[i] !=0:
                continue
            else:
                count+=1
                visited[i]=count
                queue.append(i)



bfs(r)
for i in range(1,n+1):
    print(visited[i])