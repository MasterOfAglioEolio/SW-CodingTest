
def w(a,b,c):

    if a<=0 or b<=0 or c<=0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)

    if answer[a][b][c]:
        return answer[a][b][c]

    if (a < b) and (b < c) :
        answer[a][b][c]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return answer[a][b][c]

    else:
        answer[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return answer[a][b][c]

answer=[[[0]*50 for _ in range(50)] for _ in range(50)]

while True:
    a,b,c=map(int,input().split())

    if a==-1 and b==-1 and c == -1:
        break

    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')