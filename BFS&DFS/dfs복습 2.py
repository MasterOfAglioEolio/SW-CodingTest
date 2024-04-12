n,m,r = map(int,input().split())

graph=[[] for _ in range(m+1)]

for i in range(1,m+1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[0]*(m+1)
count=1
def dfs(r):
    global count
    visited[r]=count
    graph[r].sort(reverse=True)
    for i in graph[r]:
        if visited[i] !=0:
            continue
        else:
            count+=1
            dfs(i)


dfs(r)

print(visited)