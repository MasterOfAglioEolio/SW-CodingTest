from collections import deque

n,m,s=map(int,input().split())


graph=[[] for i in range(n+1)]
visited=[False] * (n+1)
def visited_init():
    global visited
    visited=[False] * (n+1)

for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(s):

    visited[s]=True
    queue = deque()
    queue.append(s)
    while queue:
        x=queue.popleft()
        graph[x].sort()
        print(x, end=' ')
        for i in graph[x]:
            if visited[i]==True:
                continue
            else:
                queue.append(i)
                visited[i]=True

def dfs(s):
    visited[s]=True
    graph[s].sort()
    print(s,end=' ')
    for i in graph[s]:
        if visited[i]==True:
            continue
        else:
            dfs(i)

visited_init()
dfs(s)
print()
visited_init()
bfs(s)