from collections import deque
# 부분적으로 문제 해결하면서 만들어보기

# 1. 공격자 선정
# 1) 공격자 : 현재 가장 약한 포탑
# 1-2) 공격력이 가장 낮은 포탑이 2개이면 가장 최근에 공격한 포탑이 가장 약한 포탑
# 1-3) 모든 포탑은 시점 0에 모두 공격한 경험이 있다면
# 1-4) 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 "행과 열의 합"이 "가장 큰" 포탑이 가장 약한 포탑입니다.
# 1-5) 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 큰 포탑이 가장 약한 포탑입니다.
# 1-final) 공격자 공격력 + N + M

# 가장 약한 포탑 초기화
INF=(1e9)


def choice_attack(maps):
    weak_power=INF
    weak_poto = []
    count = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j]<weak_power and maps[i][j]>=1:
                weak_power=maps[i][j]

    # 맵 탐색하면서 가장 약한 포탑 추가
    for i in range(n):
        for j in range(m):
            if maps[i][j]==weak_power:
                count+=1
                weak_poto.append((i,j))
    print("weak_power {}, {} 개".format(weak_power,count))
    print(weak_poto)

    if len(weak_poto)==1: # 현재 가장 약한 포탑이 1개인 경우
        idx=weak_poto[0]
        return idx
    else: # 현재 가장 약한 포탑이 2개 이상인 경우
        print('weak_power is toooo')
        recently_attack=[] # 최근 공격한 포탑 넣기
        recently_turn=0
        for x,y in weak_poto: # 가장 약한 포탑들 최근 공격 비교
            if attack_map[x][y]>recently_turn: # 가장 최근에 공격한 포탑일 경우
                recently_attack = [] # 포탑내역 초기화
                recently_turn=attack_map[x][y] # 가장 최근에 공격한 포탑 갱신
            if attack_map[x][y]==recently_turn: # 가장 최근에 공격한 포탑이 이전과 같은 횟수일 경우
                recently_turn = attack_map[x][y]
                recently_attack.append((x, y))
        if len(recently_attack)==1: # 최근 공격한 포탑이 1개일 경우
            idx=recently_attack[0]
            print("recent_attack poto",idx)
            return idx
        else: # 최근 공격한 포탑이 2개 이상인 경우
            print("recnet_attack poto twwo",recently_attack)
            max_rc=0 # 최대 행+열
            max_rc_poto=[]
            for r,c in recently_attack:
                if max_rc<r+c: # 행+열이 이전보다 클 경우
                    max_rc=r+c
                    max_rc_poto = [] # 행+열 최대 위치 초기화
                    max_rc_poto.append((r,c))
                elif max_rc==r+c: # 행+열이 이전과 같을경우
                    max_rc_poto.append((r, c))
            if len(max_rc_poto)==1:  # 행+열 최대값이 1개일 경우
                return max_rc_poto[0]
            else:
                print("max_rc_poto twwo", max_rc_poto)
                max_c = 0  # 최대 열
                max_c_poto=[]
                for r,c in max_rc_poto: # 최대 열 찾기
                    if max_c<c:
                        max_c=c
                        max_c_poto=[]
                        max_rc_poto.append((r,c))
                return max_rc_poto[0]



# 2. 공격자 공격
# 2) 자신을 제외한 가장 강한 포탑 공격
# 2-1) 공격력이 가장 높은 포탑이 2개 이상이라면, 공격한지 가장 오래된 포탑이 가장 강한 포탑 (모든 포탑은 0시점에 공격했다고 가정)
# 2-2) 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 "행과 열"의 "합이 가장 작은" 포탑이 가장 강한 포탑
# 2-3) 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 작은 포탑이 가장 강한 포탑
def attack(x,y):
    max_power=0
    attacked_poto=[]
    for i in range(n):
        for j in range(m):
            if (i,j) != (x,y): # 공격자 자기자신이 아닐 때 대상 탐색
                if maps[i][j]>max_power: # 공격력이 max보다 높을 때
                    max_power=maps[i][j]
                    attacked_poto=[]
                    attacked_poto.append((i,j))
                elif maps[i][j]==max_power: # 공격력이 이전 max와 같을 때
                    attacked_poto.append((i,j))

    if len(attacked_poto)==1: # 공격력이 가장 높은 포탑이 1개일 때
        print("max_power_poto is only one")
        return attacked_poto[0]
    else: # 공격력이 가장 높은 포탑이 2개 이상일 때
        print("max_power_poto are too")
        # 공격한지 가장 오래된 포탑 선정
        old_turn=INF
        old_turn_poto=[]
        for i,j in attacked_poto:
            if attack_map[i][j]<old_turn: # 가장 오래된 턴 갱신
                old_turn=attack_map[i][j]
                old_turn_poto=[]
                old_turn_poto.append((i,j))
            elif attack_map[i][j]==old_turn: # 가장 오래된 턴 중복일 경우
                old_turn_poto.append((i, j))

        if len(old_turn_poto)==1: # 가장 오래된 턴이 1개일 경우
            return old_turn_poto[0]
        else: # 가장 오래된 턴이 2개 이상일 경우
            #각 포탑 위치의 "행과 열"의 "합이 가장 작은" 포탑이 가장 강한 포탑
            print("old_turn_poto are too")
            min_rc=INF
            min_rc_poto=[]
            for r,c in old_turn_poto:
                if r+c <min_rc:
                    min_rc=r+c
                    min_rc_poto=[]
                    min_rc_poto.append((r,c))
                elif r+c==min_rc:
                    min_rc_poto.append((r, c))

            if len(min_rc_poto)==1: # 행+열 가장 작은거 1개일 경우
                return min_rc_poto[0]
            else: # 행+열 가장 작은거 2개 이상 경우
                print("min_rc_poto are too")
                min_c=INF # 열값이 가장 작은 포탑으로
                for r,c in min_rc_poto:
                    if c<min_c:
                        min_c=c
                return (r,min_c)



# 3. 공격 방법
# 공격을 할 때에는 레이저 공격을 먼저 시도하고, 만약 그게 안 된다면 포탄 공격을 합니다. 각 공격의 규칙은 다음과 같습니다.

# 3-2) 레이저 공격
# 3-2-1) 상,하,좌,우 4개 방향으로 움직일 수 있음
# 3-2-2) 부서진 포탑 위치는 지날 수 없다.
# 3-2-3) 가장자리에서 막힌 방향으로 진행할 경우, 반대편으로 나옴
# 3-2-4) 레이저공격은 공격 대상 포탑까지 최단 경로로 공격함 (bfs)
# 3-2-5) IF 최단 경로가 존재하지 않을 경우 : 포탑공격 return (-1)
# 3-2-6) IF 최단 경로가 2개일 경우 : 우/하/좌/상 우선 순위대로 먼저 움직인 경로가 선택됨 maps[px-1][py] == maps[px][py-1]
# 3-2-7) 최단경로가 정해졌을 경우 공격대상 : 공격자의 공격력 만큼 피해를 입음
#                             경로에 있는 대상 : 공격자의 공격력//2

# dx dy 초기화
dx=[0,1,0,-1]
dy=[1,0,-1,0]



# 레이저 공격 함수 bfs 최단거리
def razer_check(sx,sy,p_x,p_y,maps):

    print('start razer_attack')
    print('target',p_x,p_y)

    #bfs로 최단경로 관리
    queue=deque()
    queue.append((sx,sy))

    # 공격자 방문처리
    vis[sx][sy]=True
    # 레이저 공격 시작점 초기화
    short_cut_maps[sx][sy] = 1

    # 공격 도달여부 체크
    can_attack=False

    while queue:
        x,y=queue.popleft()

        if x==p_x and y==p_y:
            print('can attack')
            can_attack=True
            print('break')
            break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # print(nx,ny) # check

            # 레이저가 가장자리를 지나는 경우 반대편으로 나옴
            if nx<0:
                nx=nx+n
            elif ny<0:
                ny=ny+m
            elif nx>=n:
                nx=nx-n
            elif ny>=m:
                ny=ny-m

            # 이미 방문한 경로라면
            if vis[nx][ny]:
                continue

            # 레이저가 부서진 포탑을 만난경우
            if maps[nx][ny] == 0:
                continue

            # 최단 경로 탐색 중 방문하지 않은 경우
            # print(vis[nx][ny],nx,ny)

            vis[nx][ny]=True
            # 최단 경로 맵 거리 계산
            short_cut_maps[nx][ny] = short_cut_maps[x][y] + 1

            back_x[nx][ny]=x
            back_y[nx][ny]=y
            print(nx, ny,x,y)
            queue.append((nx,ny))

    # 도달 가능하다면 공격 진행
    if can_attack:
        print("can attack!!")
        #가장 강한 포탑에 power 만큼 공격
        maps[p_x][p_y]-=maps[sx][sy]
        attack_map[sx][sy] += 1

        # 기존 경로 역추적해서 경로상 모든 포탑에게 power//2 만큼 공격 진행
        cx=back_x[p_x][p_y]
        cy=back_y[p_x][p_y]
        print("cx,cy",cx,cy,sx,sy)
        while not (cx==sx and cy ==sy):

            maps[cx][cy]-=(maps[sx][sy]//2)
            next_cx=back_x[cx][cy]
            next_cy=back_y[cx][cy]

            cx=next_cx
            cy=next_cy

    return can_attack




# 3-3) 포탄 공격
# 3-3-1) 공격대상은 공격자의 공격력 만큼 피해를 입음
# 3-3-2) 주위 8 방향에있는 포탑도 피해를 입음 (공격자의 공격력//2)
# 3-3-3) 공격자는 영향을 받지 않음
# 3-3-4) 만약 가장자리에 포탄이 떨어졌다면 레이저처럼 반대편 격자에 미침

# dx dy 8방향 초기화
#    동,남,서,북,동남,서남,북동,북서
dx_8=[0,1,0,-1,1,1,-1,-1]
dy_8=[1,0,-1,0,1,-1,1,-1]
def poto_attack(x,y,p_x,p_y,maps):

    #공격 대상은 공격자의 공격력만큼 피해
    maps[p_x][p_y]-=maps[x][y]

    #8 방향 공격 (절반 데미지)
    for i in range(8):
        nx=p_x+dx_8[i]
        ny=p_y+dy_8[i]
        # 포탑 주변 공격 가장자리를 지나는 경우 반대편 격자에 미침
        if nx < 0:
            nx = nx + n
        if ny < 0:
            ny = ny + m
        if nx >= n:
            nx = nx - n
        if ny >= n:
            ny = ny - m

        # 공격자는 영향을 받지 않음
        if (nx!=x) and (ny!=y):
            maps[nx][ny]-=(maps[x][y]//2)




# 4. 포탑 부서짐
# 4-1) 공격을 받아 공격력이 0 이하가 된 포탑은 부서짐

def broken_poto_check(maps):

    print("check broken poto")
    for i in range(n):
        for j in range(m):
            if maps[i][j]<=0:
                maps[i][j]=0

    return maps



# 5. 포탑 정비
# 5-1) 공격이 끝나고
# 5-2) 부서지지않은 포탑 중 공격과 무관했던 포탑은 공격력 +1
#      (공격과 무관하다 : 공격자 X AND 피해포탑 X)

def maintain_poto(maps,bef_maps,x,y):
    # print("check maintain")
    for i in range(n):
        for j in range(m):
            # 이전 맵이랑 똑같고, 0이 아니고, 공격자가 아니면 공격과 무관한 포탑
            if maps[i][j]==bef_maps[i][j] and maps[i][j]!=0 and (i,j) != (x,y):
                maps[i][j]+=1
    print('bef maps')
    for i in range(n):
        print(bef_maps[i])
    bef_maps=maps
    # print('bef change')
    # for i in range(1, n + 1):
    #     print(bef_maps[i][1:])
    return maps



# 결과 : 전체 과정이 종료된 후 가장 강한 포탑의 공격력


def solution(maps):

    for i in range(k):
        # 1.공격자 선정
        print(choice_attack(maps))
        x,y= choice_attack(maps)
        # 공격자 공격력 + M + N
        maps[x][y]=maps[x][y]+n+m
        print("choice{} upgrade power {}".format((x,y),maps[x][y]))

        # 2. 공격 대상 선정
        p_x,p_y=attack(x,y)
        print("we attack",p_x,p_y)

        # 레이저 동선 체크 가능하면 공격
        short_cut=razer_check(x, y, p_x, p_y, maps)
        print('sc',short_cut)
        # 레이저로 공격이 불가능 한 경우
        if short_cut==0:
            poto_attack(x,y,p_x,p_y,maps)

        # 4. 포탑 부서짐 체크
        broken_poto_check(maps)

        # 5. 포탑 정비
        maintain_poto(maps,bef_maps,x,y)

        max_power=[]
        # 맵 확인
        print("{} attack final",i)
        for i in range(n):
            print(maps[i])
        print("----------")
        for i in range(n):
            print(maps[i])
            max_power.append(max(maps[i]))
        print("최고 데미지:",max(max_power))
        print(short_cut)
        # if short_cut==0: # 최단 경로가 존재하지 않는경우
        #     poto_attack(x,y,p_x,p_y,maps)




# n x m 정보 / k = 턴 개수
n,m,k =map(int,input().split())

# 최근 턴 초기화
recent_turn=0

# 맵 초기화
maps=[[0]*(m) for _ in range(n)]

# 빛 공격할 때 방문여부와 경로 방향 기록
vis=[[0]*(m) for _ in range(n)]

back_x = [[0]*(m) for _ in range(n)]
back_y = [[0]*(m) for _ in range(n)]

# 피해 포탑 체크
bef_maps=[[0]*(m) for _ in range(n)]

# 최단 경로 초기화
short_cut_maps = [[0] * (m) for _ in range(n)]

# 어택 횟수 초기화
attack_map=[[0]*(m) for _ in range(n)]

# 최대 공격력 포탑
max_power=[]

for i in range(n):
    maps[i]=list(map(int,input().split()))
    bef_maps[i]=maps[i][:]

print("maps",maps)
for i in range(n):
    print(maps[i])

for i in range(n):
    print(bef_maps[i])

solution(maps)


# 4 4 2
# 0 1 4 4
# 8 0 26 13
# 8 0 26 26
# 0 1 1 2


# 4 4 1
# 0 1 4 4
# 8 0 10 13
# 8 0 11 26
# 0 0 0 0