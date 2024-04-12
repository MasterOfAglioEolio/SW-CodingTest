def is_range(x,y):
    return 1<= x and x<=n and 1<=y and y<=n

# 1 ~ P 번까지 P명의 산타 존재
# n : 게임판 크기
# m : 턴 수
# p : 산타 수
# c : 루돌프 힘
# d : 산타 힘
n,m,p,c,d = map(int,input().split())
rudolf=tuple(map(int,input().split()))

points=[0 for _ in range(p+1)]
pos=[(0,0) for _ in range(p+1)]
board=[[0]*(n+1) for _ in range(n+1)]
is_live=[False for _ in range(p+1)]
stun=[0 for _ in range(p+1)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

board[rudolf[0]][rudolf[1]]=-1

# id, x y 좌표 입력
# id별 postion 입력
# board에 위치 입력
# 생존 여부 입력
for _ in range(p):
    id,x,y=tuple(map(int,input().split()))
    pos[id]=(x,y)
    board[pos[id][0]][pos[id][1]]=id
    is_live[id]=True


# 거리 계산
INF=1e9
for t in range(1,m+1):
    closetX, closetY, closetIdx=INF,INF,0

    # 살아있는 산타 중 가장 가까운 산타 찾기
    for i in range(1,p+1):
        if not is_live[i]:
            continue

        currentBest=((closetX-rudolf[0])**2 + (closetY-rudolf[1])**2,(-closetX,-closetY))
        currentValue=(((pos[i][0]-rudolf[0])**2 + (pos[i][1]-rudolf[1])**2),(-pos[i][0],-pos[i][1]))

        if currentValue<currentBest:
            closetX,closetY=pos[i]
            closetIdx=i

    # 가장 가까운 산타의 방향으로 루돌프가 이동
    if closetIdx:
        prevRudolf = rudolf
        moveX=0

        if closetX> rudolf[0]:
            moveX=1
        elif closetY<rudolf[0]:
            moveX=-1

        moveY=0

        if closetY>rudolf[1]:
            moveY=1
        elif closetY<rudolf[1]:
            moveY=-1

        rudolf=(rudolf[0]+moveX, rudolf[1]+moveY)
        board[prevRudolf[0]][prevRudolf[1]]=0

    # 루돌프의 이동으로 충돌한 경우, 산타 이동시키고 처리
    if rudolf[0]==closetX and rudolf[1]==closetY:
        firstX = closetX+moveX*c
        firstY = closetY+moveY*c
        lastX, lastY = firstX, firstY

        stun[closetIdx]=t+1

        # 만약 이동한 위치에 산타가 있을 경우 연쇄적으로 이동
        while is_range(lastX,lastY) and board[lastX][lastY]>0:
            lastX+=moveX
            lastY+=moveY

        # 연쇄적으로 충돌이 일어난 경우 가장 마지막에서 시작
        # 순차적으로 보드판 산타 한칸씩 이동
        while not (lastX == firstX and lastY == firstY):
            beforeX =lastX-moveX
            beforeY =lastY-moveY

            if not is_range(beforeX,beforeY):
                break

            idx=board[beforeX][beforeY]

            if not is_range(lastX, lastY):
                is_live[idx]=False
            else:
                board[lastX][lastY]=board[beforeX][beforeY]
                pos[idx]=(lastX,lastY)

            lastX,lastY=beforeX,beforeY

            points[closetIdx]+=c
            pos[closetIdx]=(firstX,firstY)
            if is_range(firstX,firstY):
                board[firstX][firstY]=closetIdx
            else:
                is_live[closetIdx]=False

        board[rudolf[0]][rudolf[1]]=-1;

        # 각 산타들 루돌프와 가장 가까운 방향으로 이동

        for  i in range(1,p+1):
            if not is_live[i] or stun[i]>=t:
                continue

            minDist=(pos[i][0]-rudolf[0])**2+(pos[i][1]-rudolf[1])**2
            moveDir=-1

            for dir in range(4):
                nx=pos[i][0]+dx[dir]
                ny=pos[i][1]+dy[dir]

                if not is_range(nx,ny) or board[nx][ny]>0:
                    continue

                dist=(nx-rudolf[0])**2+(ny-rudolf[1])**2
                if dist<minDist:
                    minDist=dist
                    moveDir=dir

            if moveDir !=-1:
                nx=pos[i][0]+dx[moveDir]
                ny=pos[i][1]+dy[moveDir]

                # 산타의 이동으로 충돌한 경우, 산타를 이동시키고 처리
                if nx==rudolf[0] and ny==rudolf[1]:
                    stun[i]=t+1

                    moveX=-dx[moveDir]
                    moveY=-dy[moveDir]

                    firstX=nx+moveX*d
                    firstY=ny+moveY*d
                    lastX,lastY=firstX,firstY

                    if d==1:
                        points[i]+=d
                    else:
                        #이동한 위치에 산타가 있는 경우, 연쇄적으로 이동
                        while is_range(lastX,lastY) and board[lastX][lastY]>0:
                            lastX+=moveX
                            lastY+=moveY

                        # 연쇄적으로 충돌이 일어난 가장 마지막에서 시작해서
                        # 순차적으로 산타 한칸씩 이동
                        while lastX != firstX or lastY != firstY:
                            beforeX=lastX-moveX
                            beforeY=lastY-moveY

                            if not is_range(beforeX,beforeY):
                                break

                            idx=board[beforeX][beforeY]

                            if not is_range(lastX,lastY):
                                is_live[idx]=False
                            else:
                                board[lastX][lastY] = board[beforeX][beforeY]
                                pos[idx]=(lastX,lastY)

                            lastX,lastY=beforeX,beforeY

                        points[i] +=d
                        board[pos[i][0]][pos[i][1]]=0
                        pos[i]=(firstX,firstY)
                        if is_range(firstX,firstY):
                            board[firstX][firstY]=i
                        else:
                            is_live[i]=False
                else:
                    board[pos[i][0]][pos[i][1]]=0
                    pos[i]=(nx,ny)
                    board[nx][ny]=i


    #라운드가 끝나고 탈ㄹ락하지 않은 산타들에게 점수 1증가
    for i in range(1,p+1):
        if is_live[i]:
            points[i]+=1

for i in range(1,p+1):
    print(points[i],end=" ")