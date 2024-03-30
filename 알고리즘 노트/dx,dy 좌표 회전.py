dx=[-1,0,1,0]
dy=[0,1,0,-1]
d=0
for i in range(4):
    nd=(d+3)%4 # 반시계 방향으로 회전 (3->2->1->0)
    print(nd)
    d=nd
