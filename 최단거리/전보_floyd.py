# N개의 도시 있음
# X->Y로 메시지 보내려면 X->Y 통로가 있어야함 (일정시간 소요됨)
# X->Y 통로 있지만, Y->X 통로 없으면 메시지 못보냄

# C라는 도시에서 메시지 보냄
# 1) C에서 보낸 메시지를 받게 되는 도시의 개수
# 2) 도시들이 모두 메시지를 받는 데 까지 걸리는 시간

# 도시의 개수 N 통로의 개수 M 메시지를 보내고자 하는 도시 C
n,m,c =map(int,input().split())

INF = int(999)

graph=[[INF]*(n+1) for _ in range(n+1)]



for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x][y]=z

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

time=0
count=0

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]>=INF:
            continue
        else:
            count+=1
            if time<graph[a][b]:
                time=graph[a][b]

print(count, time)
# 3 2 1
# 1 2 4
# 1 3 2