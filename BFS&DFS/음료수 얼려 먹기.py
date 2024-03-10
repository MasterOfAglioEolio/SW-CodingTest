

n,m=map(int,input().split())

print(n,m)
graph=[]
for i in range(n):
    data_list=list(map(int,input()))
    graph.append(data_list)

def dfs(x,y):
    #주어진 범위를 벗어나는 경우 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 방문하지 않았다면
    if graph[x][y]==0:
        graph[x][y]=1
        #상 하 좌 우 위치도 모두 재귀 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i,j)==True:
            result+=1

print(result)


# 00110
# 00011
# 11111
# 00000