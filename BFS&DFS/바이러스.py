import sys
from collections import deque

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]
visited=[False]* (n+1)
for i in range(1,m+1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(data):
    queue=deque()
    queue.append(data)
    visited[data]=True
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if visited[i]==True:
                continue
            else:
                visited[i]=True
                queue.append(i)



bfs(1)

print(sum(visited)-1)






