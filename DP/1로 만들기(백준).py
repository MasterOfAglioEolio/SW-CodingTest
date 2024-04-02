# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 1로 만들 때까지 반복 (바텀업)

n=int(input())

dp=[1001]*(n+1)

dp[1]=0

if n>=2:
    dp[2] = 1
if n>=3:
    dp[3] = 1

for i in range(4,n+1):

    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)

    dp[i]=min(dp[i],dp[i-1]+1)

print(dp[n])

