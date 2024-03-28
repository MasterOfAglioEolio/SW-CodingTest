# 보드 크기 N, 사과 개수 K
# K개의 줄에는 사과의 위치가 주어짐 (행,열)
# 뱀의 방향 변환 횟수 L (X,C)
# X초가 끝난 뒤에는 C(방향) 으로 90도 회전 C : L(왼쪽) D(오른쪽)

# 사과를 먹으면 뱀 길이가 늘어남
# 벽에 부딪히면 끝남
# 처음엔 오른쪽을 향함
def turn(direction):
    global direction_num
    global n
    if direction=='L':
        direction_num-=1
        if direction_num<0:
            direction_num=3
    if direction=='D':
        direction_num+=1
        if direction_num>3:
            direction_num=0

    return direction_num

n=int(input())
graph=[[0]*n for _ in range(n)]

k=int(input())
apple=[]

for i in range(k):
    apple.append(tuple(map(int,input().split())))
    graph[apple[i][0]-1][apple[i][1]-1]=1


l=int(input())
direction=[]
for i in range(l):
    direction.append(tuple(input().split()))

dx=[-1,0,1,0]
dy=[0,-1,0,1]

position=(0,0)
time=0
x,y=0,0
direction_num=2
length=1
count=0
while True:
    time+=1

    nx=x+dx[direction_num]
    ny=y+dy[direction_num]
    print(nx,ny)
    if int(direction[count][0]) == time:
        turn(direction[count][1])
        print(direction_num)
        if count < len(direction) - 1:
            count += 1

    if nx<0 or ny<0 or nx>=n or ny>=n :
        break
    else:
        if (nx, ny) in apple:
            length += 1
            graph[nx][ny] = 0
    x=nx
    y=ny
print(time)




# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L