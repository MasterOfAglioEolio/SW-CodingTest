n=int(input())

schedule={}

for i in range(n):
    t,p=map(int,input().split())
    schedule[i]=(t,p)

# schedule[1][0] = 1일차 상담에 걸리는 시간
# schedule[1][1] = 1일차 보수

# dp로 조지기
dp=[0]*(n+1)

# 0일차 부터 n 비교
for i in range(n):
    # 의미 : 1일차 때 3일일하면 > 4일됨 즉 4일차 보수 = 1일에 시작한 일
    #       5일차 : 1일차 보수 + 4일차 보수의 합 ~
    #       7일차 : 1일차 + 4일차 + 5일차 보수의 합
    for j in range(i+schedule[i][0],n+1):
        # 기존의 dp[j] ex ) 4일차가 x일차 까지의 보수 + x일의 기간 + x일차의 보수
        if dp[j]<dp[i] + schedule[i][1]:
            dp[j]=dp[i]+schedule[i][1]


print(dp)



print(dp[-1])