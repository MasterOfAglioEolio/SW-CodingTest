# 1번부터 N번까지의 회사가 있다
# 특정 회사끼리는 서로 도로를 통해 연결되어 있음
# A 시작점은 1번 회사 위치 -> X번 회사에 방문해 물건 판매
# 연결된 2개의 회사는 양방향 이동 가능
# 특정 회사와 다른 도로로 연결되어 있다면 1만큼 시간으로 이동 가능

# A는 1번-> K번 -> X번 회사로 가는 것이 목표 (최단 거리)

n,m = map(int,input().split())

print(n,m)

INF=int(1e9)

graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x,k = map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

distance = graph[1][k]+graph[k][x]

for a in range(n+1):
    print(graph[a])



if distance >= INF:
    print(-1)
else:
    print(distance)


# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5