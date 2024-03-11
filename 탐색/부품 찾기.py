n = int(input())
n_data=list(map(int,input().split()))
m=int(input())
m_data=list(map(int,input().split()))

print(n,m,n_data,m_data)
answer=[]
for i in range(m):
    for j in range(m):
        if m_data[i] in n_data:
            answer.append("yes")
            break
        else:
            answer.append("no")
            break

for i in answer:
    print(i,end=' ')




# 5
# 8 3 7 9 2
# 3
# 5 7 9