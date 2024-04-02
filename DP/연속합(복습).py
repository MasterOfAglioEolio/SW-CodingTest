
n=int(input())
data=list(map(int,input().split()))
def max_subarray(data):
    current_sum=data[0]
    max_sum=data[0]

    for i in range(1,n):
        current_sum=max(data[i],data[i]+current_sum)
        max_sum=max(max_sum,current_sum)

    return max_sum

print(max_subarray(data))
