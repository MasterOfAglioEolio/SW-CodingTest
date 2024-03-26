# 모험가 N명
# 공포도 측정 -> 콩포도가 X인 모험가는 반드시 X명 이상으로 구성
# 최대 몇개의 그룹을 만들 수 있는가?

n=int(input())

data = list(map(int,input().split()))
data.sort()

result = 0
count = 0

for i in data: # 공포도가 낮은 것 부터 하나씩
    count+=1 # 현재 그룹에 모험가 포함시키기
    if count >= i: # 해당 그룹에 포함된 모험가 수가 현재의 공포도 이상이라면 그룹 결성
        result+=1
        count=0

print(result)

# 5
# 2 3 1 2 2