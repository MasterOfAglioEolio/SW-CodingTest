n,m = map(int,input().split())
data_list=[]
for i in range(n):
    data_list.append(list(map(int,input().split())))

max=0
result=0
for i in range(n):
    if min(data_list[i])>max:
        max=min(data_list[i])
        result=max

print(result)

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4