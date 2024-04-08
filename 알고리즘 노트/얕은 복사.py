for i in range(n):
    maps[i]=list(map(int,input().split()))
    bef_maps[i]=maps[i][:]  #이러면 maps의 변화가 bef_maps에 영향을 안끼침