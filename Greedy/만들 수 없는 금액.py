# 만들 수 없는  금액 만들기 (최소값)

# 1) 처음에 금액을 1을 만들 수 있는지 확인
# 2) ~~

n = int(input())
money=list(map(int,input().split()))

money.sort()

min_cost=1

for i in money:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if min_cost<i:
        break
    min_cost+=i

print(min_cost)