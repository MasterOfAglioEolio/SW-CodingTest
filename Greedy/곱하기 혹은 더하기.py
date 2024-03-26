# 문자열 s가 주어졌을 때
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자 확인하면서 x 혹은 + 연산자

# 1) 0~1인지 확인 하고 0~1이면 더하기
# 2) 2이상이면 곱하기

numbers=list(map(int,input()))
result=0
for i in numbers:
    if i<2:
        result+=i
    else:
        if result>=1:
            result*=i
        else:
            result=1
            result*=i

print(result)

#02984