# 구성
# 왼쪽 상단 (1,1)
# 구성 : 빈칸, 함정, 벽 (체스판 밖도 벽으로 간주)

# 조건
# 각 기사 위치 (r,c) / 기사 체력 k
# 자신의 마력으로 상대방 밀쳐낼 수 있음
# 방패 : r,c를 좌측 상단으로 h(높이)*w(너비) 크기 직사각형

# 기능 구현
# 1. 이동 : 상하좌우 이동 가능
# if 이동 위치 == 1) 이동 위치에 다른 기사가 있으면 그 기사 한칸 밀려남
#                2) 그 옆에 또 기사 있으면 연쇄적으로 또 밀림
#                3) 이동 방향의 끝에 벽이 있다면 모든 기사 이동 x

# 체스판에서 사라진 기사는 명령을 내려도 아무 반응 x

# 2. 대결 : 1) 명령을 받은 기사가 다른 기사를 밀치게 되면 밀려난 기사들은 피해를 입음
#          2) 이때 각 기사들은 해당 기사가 이동한 곳에서 w×h 직사각형 내에 놓여 있는 함정의 수만큼만 피해를 입게 됩니다
#          3) 각 기사마다 피해를 받은 만큼 체력이 깎임
#          4) 현제 체력 이상의 데미지를 받을 경우 체스판에서 사라짐
#          5) 명령을 받은 기사는 피해 X
#          6) 기사들은 밀린 이후 데미지를 입음
#          7) 밀렸더라도 밀쳐진 위치에 함정이 없으면 피해 x


# Q 번에 걸쳐 왕의 명령이 주어졌을 때, Q 번의 대결이 모두 끝난 후 생존한 기사들이 총 받은 대미지의 합을 출력

L,N,Q = map(int,input().split())
maps=[[2]*(L+1) for _ in range(L+1)]
# 0 빈칸, 1 함정, 2, 벽
# 좌표 시작은 (1,1) 이기 때문에 사이드 2으로
for i in range(1,L+1):
    temp_list = list(map(int, input().split()))
    for j in range(1,L+1):
        maps[i][j]=temp_list[j-1]
    print(maps[i])
print(maps)

# 기사 (r, c) 위치 (좌측 상단 꼭지점 기준)  h (세로 길이) w (가로 길이) k (체력)
# 처음 주어지는 기사의 위치는 기사들끼리 서로 겹쳐져 있지않음
# 기사와 벽은 겹쳐서 주어지지 않음

knight_data=[[]] # 기사 i위치 맞추기 위해 첫번째 리스트는 공백
for i in range(1,N+1):
    r,c,h,w,k=map(int,input().split())
    knight_data.append([r,c,h,w,k])
print(knight_data)

# i : i번 기사를 지칭한다.
# d : 기사에게 방향 d로 한칸 이동 (0 : 위 , 1 : 오른쪽, 2 : 아래 ,3 : 왼쪽)
# move : i,d 저장
move=[]
for i in range(Q):
    i,d=map(int,input().split())
    move.append([i,d])
print(move)

# maps : 전체 맵
# knight : 기사 데이터
# move : 명령

# 기사의 영역 계산 = knight_data (r,c) ~ (r+h , c+w)
#                 ex) r,c : 1,2  w,h : 2,1 -> (1,2) ~ (3,3) -> (1,2)~ (2,2)

# 기사 maps 추가 해당 위치에 1~3까지 표시
knight_maps=[[0]*(L+1) for _ in range(L+1)]

knight=[[]]

for i in range(1,N+1):
    knight.append([[knight_data[i][0],knight_data[i][1]],[knight_data[i][0]+knight_data[i][2]-1,knight_data[i][1]+knight_data[i][3]-1]])
    for s,e in knight[i]:
        knight_maps[s][e]=i

print(knight)
print(knight_maps)
# Q: 명령 계산
# i : i번 기사를 지칭한다.
# d : 기사에게 방향 d로 한칸 이동 (0 : 위 , 1 : 오른쪽, 2 : 아래 ,3 : 왼쪽)

dx=[-1,0,1,0]
dy=[0,1,0,-1]


# q : 명령 수
# k : 기사 위치
for q in range(Q):
    i,d=move[q]
    print("id: {}",i,d)
    # nx,ny 시작점 끝점 위치 2개 저장할 수 있는 nx[0], nx[1], ny[0], ny[1] 저장
    nx=[0]*2
    ny=[0]*2
    for x,y in (knight[i]):
        nx[k]=x+dx[d]
        ny[k]=y+dy[d]

    print(nx,ny)
