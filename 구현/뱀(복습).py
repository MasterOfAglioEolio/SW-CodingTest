n= int(input())
k=int(input())

data=[[0]*(n+1) for _ in range(n+1)] # 맵 정보
info=[] #방향 정보

# 맵 정보 (사과 표시)

for _ in range(k):
    a,b=map(int,input().split())
    data[a][b]=1

# 방향 회전 정보

l = int(input())
for _ in range(l):
    x,c=input().split()
    info.append((int(x),c))

# 동 남 서 북
dx=[0,1,0,-1]
dy=[1,0,-1,0]


def turn(direction,c):
    if c == 'L':
        direction=(direction-1)%4

    else:
        direction=(direction+1)%4

    print(direction)
    return direction

def simulate():
    x,y=1,1 # 뱀의 머리 위치
    data[x][y]=2 # 뱀이 존재하는 위치는 2
    direction=0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 시간
    index = 0 # 회전 정보
    q=[(x,y)] # 뱀이 차지하고 있는 위치 정보 (꼬리가 앞 순서)

    while True:

        nx=x+dx[direction]
        ny=y+dy[direction]

        #뱀의 위치가 유효한가 and 몸통이 없어야함
        if nx>=1 and ny>=1 and nx<=n and ny<=n and data[nx][ny]!=2:
            #사과가 없다면 다음위치
            if data[nx][ny] == 0 :
                data[nx][ny]=2
                q.append((nx,ny))
                px,py=q.pop(0)
                data[px][py]=0
            # 사과가 있다면 이동 후에 꼬리 그대로
            if data[nx][ny] ==1:
                data[nx][ny]=2
                q.append((nx,ny))
        # 몸이나 벽에 부딪힐 경우
        else:
            time+=1
            break
        x,y=nx,ny
        time+=1
        if index<l and time == info[index][0]: # 회전 타임
            direction=turn(direction, info[index][1])
            index+=1



    return time

print(simulate())