n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())

count=0
for i in range(n):
    cal=a[i]
    if cal>0:
        cal=cal-b
        count+=1
    if cal>0:
        count+=cal//c
        if cal%c>0:
            count+=1


print(count)