# 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, (바텀 업)
# 이제까지 선택된 수의 합이 최대가 되는 경로
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택

n=int(input())

data=[]
for i in range(n):
    data.append(list(map(int,input().split())))

sum_arr=[[0]*n for _ in range(n)]

if n>=1:
    sum_arr[0][0]=data[0][0]

for i in range(1,n):
    for j in range(len(data[i])):
        if j==0:
            sum_arr[i][j]=data[i][j]+sum_arr[i-1][j]
        elif j==len(data[i]):
            sum_arr[i][j]=data[i][j]+sum_arr[i-1][j-1]
        else:
            sum_arr[i][j]=max(data[i][j]+sum_arr[i-1][j-1],data[i][j]+sum_arr[i-1][j])

#   1 0  / 1 1
# 2 0 / 2 1 / 2 2

print(max(sum_arr[n-1]))