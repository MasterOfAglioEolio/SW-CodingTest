# 서로 무게가 다른 볼링공


n,m = map(int,input().split())

data=list(map(int, input().split()))
count=0
for i in range(n-1):
    for j in range(i+1,n):
        if data[i]!=data[j]:
            count+=1

print(count)

# 5 3
# 1 3 2 3 2