import sys
sys.setrecursionlimit(150000)

n,m,r = map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
visited=[0]*(n+1)
cnt=1

def dfs(data):
    global cnt
    visited[data]=cnt
    graph[data].sort()
    for i in graph[data]:
        if visited[i]==0:
            cnt+=1
            dfs(i)

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(r)
for i in range(1,n+1):
    print(visited[i])