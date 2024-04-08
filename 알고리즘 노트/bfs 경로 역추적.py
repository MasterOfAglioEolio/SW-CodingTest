n,m,k=0,0,0
nx,ny,x,y=0,0,0,0
# 맵 초기화
maps=[[0]*(m+1) for _ in range(n+1)]

# 빛 공격할 때 방문여부와 경로 방향 기록
vis=[[0]*(m+1) for _ in range(n+1)]

back_x = [[0]*(m+1) for _ in range(n+1)]
back_y = [[0]*(m+1) for _ in range(n+1)]

# 피해 포탑 체크
bef_maps=[[0]*(m+1) for _ in range(n+1)]

# 최단 경로 초기화
short_cut_maps = [[0] * (m + 1) for _ in range(n + 1)]

# 어택 횟수 초기화
attack_map=[[0]*(m+1) for _ in range(n+1)]


# 최단 경로 탐색 중 방문하지 않은 경우
if short_cut_maps[nx][ny] == 0:
    vis[nx][ny] = True
    back_x[nx][ny] = x
    back_y[nx][ny] = y

    queue.append((nx, ny))
    # 최단 경로 맵 거리 계산
    # short_cut_maps[nx][ny]=short_cut_maps[x][y]+1
# 도달 가능하다면 공격 진행
if can_attack:
    # 가장 강한 포탑에 power 만큼 공격
    maps[p_x][p_y] -= maps[x][y]
    attack_map[x][y] += 1

    # 기존 경로 역추적해서 경로상 모든 포탑에게 power//2 만큼 공격 진행
    cx = back_x[p_x][p_y]
    cy = back_y[p_x][p_y]