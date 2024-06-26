import sys
sys.setrecursionlimit(150000)

n,m,r = map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
count=1
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(data):
    global count
    visited[data]=count
    graph[data].sort(reverse=True)
    for i in graph[data]:
        if visited[i] != 0:
            continue
        else:
            count+=1
            dfs(i)

dfs(r)

for i in range(1,n+1):
    print(visited[i])