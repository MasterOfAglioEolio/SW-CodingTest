# 시간이 적게 걸리는 음식부터 확인하는 Greedy 접근 방식으로 해결할 수 있다.
# 모든 음식을 시간을 기준으로 정렬한 뒤 시간이 적게 걸리는 음식부터 제거한다.
# 이를 위해 우선순위 큐를 사용하여 구현한다.
# 1-1) 초기 단계에서는 모든 음식을 우선순위 큐(최소 힙)에 삽입한다.
# 1-2) 마지막에는 K초 후 먹어야 할 음식의 번호를 출력해야하므로 우선순위 큐에 삽입할 때
# 튜플 형태(음식 시간, 음식 번호)로 삽입한다

# 2-1) 첫 단계에서 가장 적게 걸리는 음식을 뺀다.
# 2-2) 음식이 남아있는 개수 * 음식을 먹는 시간으로 빼야함

# 3-1) 시간이 남으면 2번 음식을 빼야한다.
# 3-2) 음식이 남아있는 개수 * 음식먹는 시간
# 3-3) 전체 남은시간이 뺀 시간보다 적으면 뺴지 않는다.
# 3-4) 다음으로 먹어야할 음식을 찾는다.

import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야하므로 우선순위 큐 이용

    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간

    length = len(food_times)

    # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1  # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    result = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준으로 정렬

    return result[(k - sum_value) % length][1]











