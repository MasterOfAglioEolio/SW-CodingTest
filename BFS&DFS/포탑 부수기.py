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
    for i in range(1,n+1):
        for j in range(1,m+1):
            if maps[i][j]<weak_power and maps[i][j]>=1:
                weak_power=maps[i][j]

    # 맵 탐색하면서 가장 약한 포탑 추가
    for i in range(1,n+1):
        for j in range(1,m+1):
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
            return
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
    for i in range(1,n+1):
        for j in range(1,m+1):
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
# 3-2-4) 레이저공격은 공격 대상 포탑까지 최단 경로로 공격함
# 3-2-5) IF 최단 경로가 존재하지 않을 경우 : 포탑공격
# 3-2-6) IF 최단 경로가 2개일 경우 : 우/하/좌/상 우선 순위대로 먼저 움직인 경로가 선택됨
# 3-2-7) 최단경로가 정해졌을 경우 공격대상 : 공격자의 공격력 만큼 피해를 입음
#                             경로에 있는 대상 : 공격자의 공격력//2

# 3-3) 포탄 공격
# 3-3-1) 공격대상은 공격자의 공격력 만큼 피해를 입음
# 3-3-2) 주위 8 방향에있는 포탑도 피해를 입음 (공격자의 공격력//2)
# 3-3-3) 공격자는 영향을 받지 않음
# 3-3-4) 만약 가장자리에 포탄이 떨어졌다면 레이저처럼 반대편 격자에 미침


# 4. 포탑 부서짐
# 4-1) 공격을 받아 공격력이 0 이하가 된 포탑은 부서짐

# 5. 포탑 정비
# 5-1) 공격이 끝나고
# 5-2) 부서지지않은 포탑 중 공격과 무관했던 포탑은 공격력 +1
#      (공격과 무관하다 : 공격자 X AND 피해포탑 X)

# 결과 : 전체 과정이 종료된 후 가장 강한 포탑의 공격력


def solution(maps):

    for i in range(k):
        # 공격자 선정
        x,y= choice_attack(maps)
        # 공격자 공격력 + M + N
        maps[x][y]=maps[x][y]+n+m
        print("choice{} upgrade power {}".format((x,y),maps[x][y]))

        # 공격 대상 선정
        p_x,p_y=attack(x,y)
        print("we attack",p_x,p_y)

# n x m 정보 / k = 턴 개수
n,m,k =map(int,input().split())

# 최근 턴 초기화
recent_turn=0

# 맵 초기화
maps=[[0]*(m+1) for _ in range(n+1)]

# 어택 횟수 초기화
attack_map=[[0]*(m+1) for _ in range(n+1)]
print(attack_map)

for i in range(1,n+1):
    maps[i][1:]=map(int,input().split())

for i in range(1,n+1):
    print(maps[i][1:])

solution(maps)


# 4 4 1
# 0 1 4 4
# 8 0 26 13
# 8 0 26 26
# 0 1 1 2