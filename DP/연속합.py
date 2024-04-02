
n=int(input())
data=list(map(int,input().split()))



def max_subarray_sum(data):
    max_sum=data[0]
    max_current_sum=data[0]

    for i in range(1,n):
        max_current_sum=max(data[i],max_current_sum+data[i])
        max_sum=max(max_sum,max_current_sum)

    return max_sum


print(max_subarray_sum(data))