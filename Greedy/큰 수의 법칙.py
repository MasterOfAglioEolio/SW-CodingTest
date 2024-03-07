# 본인 풀이
n,m,k = map(int,input().split())

data_list=[]*n
data_list=list(map(int,input().split()))

sum=0
count=0
recent_num=0
temp_list=[]
for i in range(m):
    current_num = max(data_list)
    temp_list=data_list[:]
    if count<k:
        sum+=current_num
        count+=1
        print(sum,current_num)
    elif count>=k:
        temp_list.pop(data_list.index(current_num))
        current_num=max(temp_list)
        sum+=current_num
        print(sum, current_num)
        count=0

print(sum)
# 5 8 3
# 2 4 5 4 6

# 답 풀이
n,m,k = map(int,input().split())
data_list=list(map(int,input().split()))

data_list.sort()
first=data_list[n-1]
second=data_list[n-2]
result=0

while True:
    for i in range(k):
        if m==0:
            break
        result +=first
        m-=1
    if m==0:
        break
    result +=second
    m-=1
print(result)