n,k=map(int,input().split())

list_a=list(map(int,input().split()))
list_b=list(map(int,input().split()))

list_a=sorted(list_a)
list_b=sorted(list_b, reverse=True)
for i in range(k):
    if list_a[i]<list_b[i]:
        list_a[i],list_b[i]=list_b[i],list_a[i]
    else:
        break



print(n,k)
print(list_a, list_b)
print(sum(list_a))
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5