# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
# 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다. -> 탑 다운(recursive)

n=int(input())
floor=[]
for i in range(n):
    floor.append(int(input()))

floor_score=[0]*n
def floor_max_score(floor):
    if n >= 1:
        floor_score[0] = floor[0]
    if n >= 2:
        floor_score[1] = floor[0] + floor[1]
    if n >= 3:
        floor_score[2] = max(floor[0] + floor[2], floor[1] + floor[2])
    if len(floor)>=4:
        for i in range(3,n):
            # 직전 계단에서 올라온 경우 vs
            # 전전 계단에서 올라온 경우
            floor_score[i]=max(floor_score[i-3]+floor[i-1]+floor[i],floor_score[i-2]+floor[i])

    return floor_score[n-1]

print(floor_max_score(floor))