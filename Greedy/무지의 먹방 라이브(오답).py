# 회전판에 N개의 음식
# 1~N 까지 증가
# 다 먹으면 다시 1번 음식 옴
# 음식 하나 1초 -> 그대로 -> 다음 음식(가장 가까운 번호)
#
def solution(food_times, k):
    answer = 0
    time = 0
    if sum(food_times)<=k:
        return -1
    while time <= k:
        for i in range(len(food_times)):
            # print(food_times)
            if time == k:
                return i + 1
            else:
                if food_times[i] != 0:
                    food_times[i] -= 1
                    time += 1
                else:
                    continue
