# 점수가 특정 조건을 만족할 때만 사용 가능
# 조건 : 현재 캐릭터의 점수를 N이라 할 때
#       자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽의 각 자릿수의 합을 더한 값이 같아야함

n=input()
print(n)
left_sum=0
right_sum=0

for i in range(len(n)//2):
    left_sum+=int(n[i])
    right_sum+=int(n[-i-1])

print(left_sum,right_sum)

if left_sum==right_sum:
    print('LUCKY')
else:
    print("READY")



#123402