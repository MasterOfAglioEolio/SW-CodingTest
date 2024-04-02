# 수열 a가 주어졌을 떄 가장 긴 증가하는 부분 수열 (바텀 없 다운)
#

n=int(input())
data=list(map(int,input().split()))

print(n,data)

dp=[1]*n

for i in range(n):
    for j in range(i):
        if data[i]>data[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))