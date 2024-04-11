
n=int(input())
schedule={}
for i in range(n):
    t,p=map(int,input().split())
    schedule[i]=(t,p)

# print(schedule)

dp=[0]*(n+1)

for i in range(n):
    for j in range(i+schedule[i][0],n+1):
        if dp[j]<dp[i]+schedule[i][1]:
            dp[j]=dp[i]+schedule[i][1]


print(dp[-1])