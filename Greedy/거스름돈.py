n=int(input())

money=[500,100,50,10]
count=0
for i in range(len(money)):
    count+=n//money[i]
    n%=money[i]

print(count)