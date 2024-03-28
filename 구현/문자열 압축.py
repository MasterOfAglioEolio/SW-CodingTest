# 연속해서 나타나는 문자의 개수, 반복되는 값으로 표현
# 문자 압축 단위가 가장 짧은 것의 길이 return
# 이전문자 저장 / 이전 문자랑 같으면 count++ / 다르면 1부터 다시

def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘러가며 확인
    for step in range(1, len(s)//2 + 1): #최대 압축 가능한 단위가 문자열 길이의 절반을 넘을 수 없기 때문
        compressed = ''
        prev = s[0:step]  # 앞에서부터 step만큼 추출
        count = 1

        # step 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나온 경우
            else:
                if count >= 2:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = s[j:j + step]
                count = 1
        # 남아있는 문자열 처리
        if count >= 2:
            compressed += str(count) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))

    return answer