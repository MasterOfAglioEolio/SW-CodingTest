from collections import deque

# 전역 변수들 정의

MAX_N = 31 # 기사의 수
MAX_L = 41 # 체스판 크기

# 기사 이동 방향
dx=[-1,0,1,0]
dy=[0,1,0,-1]

info = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)] # 체스판 초기화

bef_k = [0 for _ in range(MAX_N)] # 기사 초기 체력 초기화

r = [0 for _ in range(MAX_N)] # 기사 초기위치 r 초기화
c = [0 for _ in range(MAX_N)] # 기사 초기위치 c 초기화
h = [0 for _ in range(MAX_N)] # 기사 범위 h 초기화
w = [0 for _ in range(MAX_N)] # 기사 범위 w 초기화
k = [0 for _ in range(MAX_N)] # 기사 체력 k 초기화

nr = [0 for _ in range(MAX_N)] # 이동 좌표 r 초기화
nc = [0 for _ in range(MAX_N)] # 이동 좌표 c 초기화

dmg = [0 for _ in range(MAX_N)] # 데미지 초기화
is_moved = [False for _ in range(MAX_N)] # 명령 초기화


# 움직임 시도
def try_movement(idx,dir):
    q=deque()
    is_pos=True

    #초기화
    for i in range(1,n+1):
        dmg[i]=0
        is_moved[i]=False
        nr[i]=r[i]
        nc[i]=c[i]

    q.append(idx)
    is_moved[idx]=True

    while q:
        x= q.popleft()

        nr[x]+=dx[dir]
        nc[x]+=dy[dir]

        # 경계 체크
        if nr[x]<1 or nc[x]<1 or nr[x]+h[x]-1> l or nc[x]+w[x]-1>l:
            return False

        # 대상이 다른 대상이나 장애물과 충돌하는지 검사
        for i in range(nr[x],nr[x]+h[x]):
            for j in range(nc[x],nc[x]+w[x]):
                if info[i][j]==1: # 함정과 충돌하는 경우
                    dmg[x]+=1
                if info[i][j]==2: # 벽과 충돌하는 경우
                    return False

        # 다른 대상과 충돌하는 경우, 해당 대상 이동
        for i in range(1,n+1):

            # 이미 이동했거나 체력이 없는 기사는 무시
            if is_moved[i] or k[i] <=0:
                continue

            # 기사 i와 기사 x가 세로 방향으로 겹치지 않는 경우
            if r[i]>nr[x]+h[x]-1 or nr[x]>r[i]+h[i]-1:
                continue

            # 기사 i와 기사 x가 가로 방향으로 겹치지 않는 경우
            if c[i]>nc[x]+w[x]-1 or nc[x]>c[i]+w[i]-1:
                continue

            # 위의 두 조건을 모두 통과하지 못했다면, 겹치는 경우임
            # 겹치는 경우, 해당 기사를 이동 대상으로 설정하고 큐에 추가
            is_moved[i]=True
            q.append(i)

    dmg[idx]=0
    return True

# 특정 대상을 지정된 방향으로 이동시키는 함수
def move_piece(idx,move_dir):
    if k[idx]<=0:
        return

    #이동이 가능한 경우, 실제 위치와 체력을 업데이트
    if try_movement(idx, move_dir):
        for i in range(1,n+1):
            r[i]=nr[i]
            c[i]=nc[i]
            k[i]-=dmg[i]


# 입력값을 받는다.
l,n,q = map(int, input().split())

# 맵 정보 입력
for i in range(1,l+1):
    info[i][1:] = map(int,input().split())

# 기사 정보 입력
for i in range(1,n+1):
    r[i],c[i],h[i],w[i],k[i] = map(int,input().split())
    bef_k[i]=k[i]

# 명령 정보 입력
for _ in range(q):
    idx,d = map(int,input().split())
    move_piece(idx,d)

# 결과
ans = sum(bef_k[i]-k[i] for i in range(1,n+1) if k[i]>0)
print(ans)