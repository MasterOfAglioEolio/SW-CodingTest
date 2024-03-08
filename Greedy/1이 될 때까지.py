n,k=map(int,input().split())

count=0
result=n
while result>1:
    if result%k==0:
        result/=k
    else:
        result-=1
    count+=1

print(count)

