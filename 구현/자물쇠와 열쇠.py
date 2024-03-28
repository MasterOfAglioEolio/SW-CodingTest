# 배열을 왼쪽 위부터 한칸씩 이동하여 자물쇠의 모든 홈을 채운다.
# 즉, 1보다 크거나 작은 구간이 있으면 실패 !

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for i in range(m)]  # 결과 리스트

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result


# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠의 크기 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):

        key = rotate_a_matrix_by_90_degree(key)  # 열쇠 회전
        for x in range(n * 2):       # 원래 길이의 *2해서 중앙에 맞추기
            for y in range(n * 2):
                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                # 새로운 자물쇠에 열쇠가 정확이 맞는지 검사
                if check(new_lock) == True:
                    return True

                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False


