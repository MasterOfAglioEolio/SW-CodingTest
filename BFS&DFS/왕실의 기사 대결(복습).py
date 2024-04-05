from collections import deque
#체스판 : L x L
# 체스판 왼쪽 상단 : (1,1)
# 체스판 구성 : 빈칸, 함정, 벽

# 기사 : 초기 위치 (r,c) + h(높이) x w(너비)
# 상대방 밀쳐낼 수 있음
# 기사의 체력 : k

# 기사 이동
# 상하좌우로 이동 가능
# 이동 위치에 다른 기사있을 경우 밀쳐냄 + 그 옆에 또 있으면 또 밀쳐냄
# 이동하려는 방향의 끝에 벽이 있다면 기사 이동 x
# 체스판에서 사라지면 명령 x


# 기사 대결
# 명령 받은 기사가 다른 기사를 밀치면 밀려난 기사는 피해를 입는다.
# 각 기사들은 해당 기사가 이동한 곳에서 w x h 직사각형 내에 놓여있는 함정 수 만큼 피해를 입음
# 피해를 입는다 -> 체력이 깎인다 -> 체력이 0이 된다 -> 체스판에서 사라진다.
# 명령을 받은 기사는 피해 x
# 기사들은 밀린 후에 피해를 입음

# 입력
# L : 체스판 크기 N : 기사의 수 Q : 명령의 수
l,n,q = map(int,input().split())

# 체스판 크기 초기화
maps=[[0]*(l+1) for _ in range(l+1)]

for i in range(1,l+1):
    maps[i][1:]=map(int,input().split())

# 기사 데이터 초기화
r=[0 for _ in range(n+1)] # 시작 좌표 r 초기화
c=[0 for _ in range(n+1)] # 시작 좌표 c 초기화
h=[0 for _ in range(n+1)] # 기사 범위 h 초기화
w=[0 for _ in range(n+1)] # 기사 범위 w 초기화
bef_k=[0 for _ in range(n+1)] # 초기 체력 초기화
k=[0 for _ in range(n+1)] # 체력 초기화

nr=[0 for _ in range(n+1)] # 이동 좌표 r 초기화
nc=[0 for _ in range(n+1)] # 이동 좌표 c 초기화

is_moved=[False for _ in range(n+1)]
dmg=[0 for _ in range(n+1)] # 누적 데미지 초기화
# 기사 데이터 입력
for i in range(1,n+1):
    r[i],c[i],h[i],w[i],k[i] = map(int,input().split()) # 기사 데이터 추가
    bef_k[i] = k[i]

print(r,c,h,w,k)
print(is_moved)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def move_try(idx,dir):
    queue=deque()
    queue.append(idx)

    is_pos=True

    for i in range(1,n+1):
        dmg[i]=0
        is_moved[i]=False
        nr[i]=r[i]
        nc[i]=c[i]

    is_moved[idx]=True

    while queue:
        x= queue.popleft()

        nr[x]=nr[x]+dx[dir]
        nc[x]=nc[x]+dy[dir]

        #경계 체크
        if nr[x]<1 or nc[x]<1 or nr[x]>l or nc[x]>l:
            return False  # 함수 즉시 종료, 함수 호출 구간으로 반환

        # 벽, 함정 체크
        for i in range(nr[x],nr[x]+h[x]):
            for j in range(nc[x],nc[x]+w[x]):
                if maps[i][j]==2:
                    return False
                if maps[i][j]==1:
                    dmg[x]+=1

        #기사 충돌 체크
        # 다른 대상과 충돌하는 경우, 해당 대상 이동
        for i in range(1, n+1):
            # 이미 이동했거나, 체력이 없는 기사는 무시
            if is_moved[i] or k[i]<=0:
                continue # 현재 명령어의 반복문 건너 뜀

            # 기사 i와 기사 x의 세로 위치가 겹치지 않을 경우
            if r[i]>nr[x]+h[x]-1 or nr[x]>r[i]+h[i]-1:
                continue
            # 기사 i와 기사 x의 가로 위치가 겹치지 않을 경우
            if r[i]>nr[x]+h[x]-1 or nr[x]>r[i]+h[i]-1:
                continue

            # 위치가 겹치는 경우 이동 추가
            is_moved[i] = True
            queue.append(i)

    dmg[idx]=0
    return True

# 특정 대상을 지정된 방향으로 이동시키는 함수
def move_knight(idx,dir):
    #기사의 피가 0보다 적을 경우
    if k[idx]<=0:
        return

    if move_try(idx,dir):
        for i in range(1,n+1):
            r[i]=nr[i]
            c[i]=nc[i]
            k[i]-=dmg[i]


for _ in range(1,q+1):
    idx,dir=map(int,input().split()) #명령
    move_knight(idx,dir)

print(bef_k,k)
# 결과 ★(생존한 기사들이 받은 데미지 계산)★
ans = sum(bef_k[i]-k[i] for i in range(1,n+1) if k[i]>0)
print(ans)