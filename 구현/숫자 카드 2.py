# 숫자카드 n개에서 정수 m개가 주어졌을 때 이 수가 적혀있는 숫자 카드를 상근이가 몇개 가지고있는가


n = int(input())
n_list=sorted(list(map(int,input().split())))

m=int(input())
m_list=list(map(int,input().split()))

answer_list=[]



def binary_search(target, data,start,end):
    # print(target)
    if start>end:
        return 0

    median=(start+end)//2

    if data[median]<target:
        return binary_search(target,data,median+1,end)
    elif data[median]>target:
        return binary_search(target,data,start,median-1)
    elif data[median]==target:
        return count.get(target)


count={}
for i in n_list:
    if i in count:
        count[i]+=1
    else:
        count[i]=1


# print(count)


for target in m_list:
    print(binary_search(target,n_list,0,len(n_list)-1),end=' ')



