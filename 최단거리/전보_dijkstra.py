import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드를 만들기

n,m,start = map(int,input().split())

#각 노드에 연결되어있는 노드에 대한 정보 담기

graph = [[] for i in range(n+1)]

# 최단 거리 테이블은 모두 무한으로 초기화
distance=[INF]*(n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x,y,z=map(int,input().split())
    # x번 노드애서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y,z))

print(graph)

def dijkstra(start):
    q=[]
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q: #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] <dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost=dist+i[1]

            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

#도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중 가장 멀리있는 노드와의 최단 거리
max_distance=0

for d in distance:
    if d !=INF:
        count+=1
        max_distance=max(max_distance,d)

# 시작 노드는 제외하므로 count-1
print(count-1, max_distance)