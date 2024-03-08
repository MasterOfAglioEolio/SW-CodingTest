n=list(input())
x=n[0]
y=int(n[1])

x_position=[0,'a','b','c','d','e','f','g','h']

dx=[2,2,-2,-2,-1,1,-1,-1]
dy=[-1,1,-1,1,2,2,-2,-2]

count=0
for i in range(len(x_position)):
    if x==x_position[i]:
        for j in range(len(dx)):
            nx=i+dx[j]
            ny=y+dy[j]
            if nx<1 or ny<1 or nx>8 or ny>8:
                continue
            else:
                count+=1

print(count)

