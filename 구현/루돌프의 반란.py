
# 구현 문제
from collections import deque
# 1 ~ P 번까지 P명의 산타 존재
# n : 게임판 크기
# m : 턴 수
# p : 산타 수
# c : 루돌프 힘
# d : 산타 힘
n,m,p,c,d = map(int,input().split())

# rr,rc : 루돌프 초기 위치
rr,rc=map(int,input().split())
santa={}

# pn 산타 번호
# sr, sc : 산타 초기 위치
for i in range(1,p+1):
    pn,sr,sc=map(int,input().split())
    santa[pn]=(sr,sc)

# santa_score : 산타 점수
santa_score=[0]*(p+1)

# maps 초기화
maps=[[0]*(n+1) for _ in range(n+1)]

# 루돌프 위치 : 2
maps[rr][rc]=99

# 산타 위치 저장
for i in range(1,p+1):
    sr,sc=santa[i]
    maps[sr][sc]=i

for i in range(1,n+1):
    print(maps[i][1:])

# 산타 탈락 체크
survive=[True]*(p+1)
print(survive)
# 기절 체크
stun = [False]*(p+1)

# 방문 체크 초기화
visited=[[False]*(n+1) for _ in range(n+1)]

# 산타 움직임 방향
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 루돌프 움직임 방향
dx_8=[-1,0,1,0,-1,-1,1,1]
dy_8=[0,1,0,-1,-1,1,-1,1]

INF=(1e9)

# 2) 루돌프의 움직임
# 2-2) 가장 가까운 산타를 향해 1칸 돌진 (bfs -> 1칸 움직임) (CEHCK)
# 2-3) 단 게임에서 탈락하지 않은 산타 중 가장 가까운 산타 선택 (CHECK)
# 2-4) 가장 가까운 산타가 2명 이상이라면, r 좌표가 가장 큰 산타에게 돌진, r이 동일한 경우 c 좌표가 큰 산타를 향해 돌진 (sorted ) (CHECK)

def active_r(x,y): #루돌프 움직임
    min_dis=INF
    #산 타 거리 딕셔너리
    santa_dis={}
    # 최소거리 산타 위치 딕셔너리
    min_dict={}

    # 산타와 거리 계산
    for i in range(1,p+1):
        # 게임에서 탈락하지 않은 산타 선택
        if survive[i]==True:
            sr,sc=santa[i]
            # 거리 계산
            distance=(x-sr)**2+(y-sc)**2
            santa_dis[i]=distance
            # 최저 거리 계산
            if santa_dis[i]<min_dis:
                min_dis=santa_dis[i]
                min_dict[i]=(sr,sc)
            # 최저 거리가 2개 이상인 경우
            elif santa_dis[i]==min_dis:
                min_dict[i]=(sr,sc)
    # print(min_dis,min_count)
    # 최소 거리가 2명 이상인 경우
    if len(min_dict) > 1:
        print(len(min_dict))
        print(min_dict)
        max_r=0
        max_r_dict={}
        # r이 가장 큰 값 계산
        for i in min_dict.keys():
            if min_dict[i][0]>max_r:
                max_r=min_dict[i][0]
                max_r_dict[i]=min_dict[i]
        print(max_r_dict)
        # r이 가장 큰 값이 2개 이상인 경우
        if len(max_r_dict)>1:
            max_c=0
            max_c_santa_idx=0
            # c이 가장 큰 값 계산
            for i in max_r_dict.keys():
                if max_r_dict[i][1]>max_c:
                    max_c_santa_idx=i
            tr,tc=min_dict[max_c_santa_idx]
            move_r(x,y,tr,tc)
        # r값 최대가 1개인경우
        elif len(max_r_dict)==1:
            print("one max_r")
            tr,tc=max_r_dict
            move_r(x, y, tr, tc)
    # 최소 거리가 1개인 경우
    elif len(min_dict)==1:
        tr,tc=min_dict
        move_r(x,y,tr,tc)
    else:
        print("최소거리가 존재하지 않습니다.")
        return

    # 이동 전 루돌프 위치 0으로 만들기
    maps[x][y] = 0
    return move_r(x,y,tr,tc)

# 2-5) 루돌프는 상하좌우, 대각선을 포함한 8방향 중 하나로 돌진 가능
# 2-6) 가장 우선순위가 높은 산타를 향해 8방향 중 가장 가까워지는 방향으로 한 칸 돌진합니다.

#루돌프 움직임 계산
def move_r(x,y,tr,tc):
    # 최소거리 계산
    min_dis=INF
    min_nx,min_ny=0,0
    for i in range(8):
        nx=x+dx_8[i]
        ny=y+dy_8[i]

        # 맵의 범위 안에 있으면 거리 계산
        if 0<nx<=n and 0<ny<=n:
            distance=(nx-tr)**2+(ny-tc)**2
            if distance<min_dis:
                min_dis=distance
                min_nx=nx
                min_ny=ny

    move_point=(min_nx,min_ny,i)
    print("move",move_point,i)
    return move_point

#산타 움직임 계산
def move_s(x,y,tr,tc):
    # 최소거리 계산
    min_dis = INF
    min_nx, min_ny = 0, 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 맵의 범위 안에 있으면 거리 계산
        if 0 < nx <= n and 0 < ny <= n:
            distance = (nx - tr) ** 2 + (ny - tc) ** 2
            if distance < min_dis:
                min_dis = distance
                min_nx = nx
                min_ny = ny

    move_point = (min_nx, min_ny,i)
    print("move", move_point)
    return move_point



# 3) 산타 움직임
# 3-2) 산타는 1번부터 P번까지 순서대로 움직임 (CHECK)
# 3-3) 이미 기절했거나 탈락한 산타는 움직일 수 없음 (CEHCK)
# 3-4) 산타는 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동
# 3-5) 산타는 다른 산타가 있는 칸이나 게임판 밖으로 움직일 수 없음
# 3-6) 움직일 수 있는 칸이 있더라도 루돌프로부터 가까워질 수 없으면 움직이지 않음 (??) // 이전 거리랑 계산해서 더 가까운거 아니면 움직임 X
# 3-7) 산타는 상하좌우 4칸으로만 이동 가능
def active_s(idx): # 산타 움직임
    if survive[idx]==True:
        sx,sy=santa[idx]
        maps[sx][sy]=0
        nx,ny,direction=move_s(sx,sy,rr,rc)
        #이전 거리
        bef_dis=(sx-rr)**2+(sy-rc)**2
        #새로운 움직임 거리
        new_dis=(nx-rr)**2+(ny-rc)**2
        #더 가까울 경우만 움직임
        if new_dis<bef_dis:
            return nx,ny,direction
        else:
            return
    else:
        return


# 4) 충돌
# 4-2) 산타와 루돌프가 같은 칸에 있으면 충돌이 발생
# 4-3) 루돌프가 움직여서 충돌이 일어난 경우 -> 해당 산타 C점수 획득  / 루돌프가 이동해온 방향으로 C칸 만큼 밀림
# 4-5) 밀려나는 과정에서는 충돌이 일어나지 않고 정확히 원하는 위치에 도달함
# 4-6) 만약 밀려난 위치가 게임판 밖이면 산타는 게임 탈락 (T/F) (Check)
# 4-7) 밀려난 칸에 다른 산타 있는 경우 "5) 상호작용" 발생

# 루돌프 움직일 경우
def crush_check_r(x,y,direction):
    # 루돌프가 움직인 위치에 산타가 있는 경우
    if maps[x][y] in range(1,p+1):
        santa_score[maps[x][y]]+=c

        # 루돌프가 이동해온 거리만큼 산타 밀어내기
        nx=x-dx_8[direction]*c
        ny=y-dy_8[direction]*c

        if nx<1 or ny<1 or nx>n or ny>n:
            survive[maps[x][y]]=False
            #루돌프 움직임 갱신 / 산타 지우기
            maps[x][y]=99
        else:
            #밀려난 자리에 산타가 있는 경우
            if maps[nx][ny] in range(1,p+1):
                #상호작용 발생
                interaction(nx,ny,direction)
                maps[nx][ny]=maps[x][y]
                maps[x][y] = 99

            # 밀려난 자리에 산타가 없는 경우
            else:
                # 해당 위치로 산타 움직임
                maps[nx][ny] = maps[x][y]
                maps[x][y] = 99
    else:
        maps[x][y] = 99

    return

# 4-4) 산타가 움직여서 충돌이 일어난 경우 -> 해당 산타는 D만큼 점수 획득 / 산타는 자신이 이동해온 방향의 반대로 D만큼 밀림
# 4-5) 밀려나는 과정에서는 충돌이 일어나지 않고 정확히 원하는 위치에 도달함
# 4-7) 밀려난 칸에 다른 산타 있는 경우 "5) 상호작용" 발생

# 산타 움직일 경우
def crush_check_s(x,y,direction,j):

    # 움직인 위치에 루돌프 있는 경우
    if maps[x][y]==99:
        queue=deque()
        queue.append((x,y))
        santa_score[j]+=d

        nx=x-dx[direction]*d
        ny=y-dy[direction]*d
        # 팅겼는데 범위 벗어나는 경우
        if nx < 1 or ny < 1 or nx > n or ny > n:
            survive[j] = False
        # 팅겼는데 범위 안에 있는 경우
        else:
            #팅겼는데 다른 산타랑 부딪힌 경우
            if maps[nx][ny] in range(1,p+1):
                interaction(nx,ny,direction)
                # maps[x][y]=0
                maps[nx][ny]=j
            else:
                # maps[x][y] = 0
                maps[nx][ny] = j
    else:
        maps[x][y]=j


    return

# 5) 상호작용
# 5-2) 루돌프와 충돌 후 착지하는 칸에서만 상호작용 발생
# 5-3) 충돌후 착지한 다른 칸에 다른 산타이으면 그 산타 1칸 해당 방향으로 밀림
# 5-4) 그 옆에 산타 있으면 연쇄적으로 1칸 밀려나는 것 반복 (게임판 밖으로 밀리면 탈락) -----------일단 여기까지

def interaction(x,y,direction):
    queue=deque()
    #밀린 위치에 새로운 산타 있는 경우
    queue.append((x,y,maps[x][y]))
    print(queue)
    while queue:
        x,y,idx=queue.popleft()
        print("{},{} 상호작용 발생".format(x,y))
        #새로운 산타 밀리는 위치
        nx=x-dx_8[direction]
        ny=y-dy_8[direction]
        #범위 벗어나는 경우
        if nx<1 or ny<1 or nx>n or ny>n:
            #탈락
            survive[idx]=False
        #범위 안에 있는 경우
        else:
            #범위 안에 또 산타 있는 경우
            if maps[nx][ny] in range(1,p+1):
                #큐에 추가
                queue.append((nx,ny,maps[nx][ny]))
                maps[nx][ny]=idx


# 6) 기절
# 6-2) 산타는 루돌프와 충돌 후 기절함
# 6-3) ex) 현재가 k번째 턴이면 k+1번째 턴까지 기절해서 k+2턴 부터 다시 정상
# 6-4) 기절한 탄사는 움직일 수 없지만 / 기절 도중 충돌이나 상호작용으로 밀려날 수 있음
# 6-5) 루돌프는 기절한 산타에게 돌진 가능

# 1) 게임판 구성
# 1-2) N x N 격자 각 위치 (r,c) 아래로 갈수록 r증가 오른쪽 갈수록 c 증가 /좌 상단 : 1,1  (CHECK)
# 1-3) 게임은 총 M개의 턴에 걸쳐서 진행 / 매 턴마다 루돌프와 산타들이 한 번씩 움직임 (CHECK)
# 1-4) 루돌프 한 번 움직인 후 -> 1번 산타 ~ P번 산타 움직임 (CHECK)
# 1-5) 기절하거나 격자 밖으로 빠져나간 산타는 움직일 수 없음 (CHECK)
# 1-6) 게임에서 두 칸 사이의 거리 : (r1 c1) (r2 c2) -> (r1-r2)^2 + (c1-c2)^2 (CHECK)

# 7) 게임종료
# 7-2) M번의 턴을 거쳐 루돌프, 산타 움직이면 게임 종료
# 7-3) P명의 산타 모두 탈락하면 그 즉시 게임 종료 (if not santa
# 7-4) 매 턴 이후 아직 탈락하지 않은 산타들에겐 1점씩 부여 (check)

def check_survived():
    for i in range(1,p+1):
        if survive[i]==True:
            santa_score[i]+=1
    print("santa_score",santa_score[1:])

def solution():
    for i in range(1,2):
        # 루돌프 움직임
        nx,ny,direction_r=active_r(rr,rc)
        print("루돌프 {} 번째 움직임 {}, {} dir {}".format(i,nx,ny,direction_r))
        crush_check_r(nx,ny,direction_r)
        #산타 움직임
        for j in range(1,p+1):
            nsx,nsy,direction_s=active_s(j)
            print("{}번 산타 {} 번째 움직임 {}, {} dir{}".format(j,i, nsx, nsy,direction_s))
            crush_check_s(nsx,nsy,direction_s,j)

        check_survived()




# 게임이 끝나고 각 산타가 얻는 최종 점수 구하라 !
# 각 산타가 얻은 최종 점수를 1번부터 P번까지 순서대로 공백을 사이에 두고 출력합니다.

solution()

for i in range(1,n+1):
    print(maps[i][1:])