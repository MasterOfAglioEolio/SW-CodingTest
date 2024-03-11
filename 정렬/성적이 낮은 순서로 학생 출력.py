n=int(input())

stu={}
for i in range(n):
    name,score=input().split()
    stu[name]=int(score)


print(sorted(stu.keys()))
# 2
# 홍길동 95
# 이순신 77