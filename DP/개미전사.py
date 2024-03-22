# 식량창고 여러개, 식량창고는 일직선
# 최소 한 칸 이상 떨어진 식량창고를 약탈해야함

n=int(input())
array=list(map(int,input().split()))

# DP 테이블 초기화
data=[0]*100


# DP 진행 (바텀업)
data[0]=array[0]
data[1]=max(array[0],array[1])
for i in range(2,n):
    data[i]=max(data[i-1],data[i-2]+array[i])

print(data[n-1])
# 4
# 1 3 1 5
