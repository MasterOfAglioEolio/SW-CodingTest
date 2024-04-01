
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def fibonacci(n):
    f = [0] * (n+1)
    count=0
    if n==1 :
        f[1]=1
    elif n==2:
        f[2]=1
    else:
        for i in range(3,n+1):
            count+=1
            f[n]=f[n-2]+f[n-1]
        return count

n=int(input())
print(fib(n),fibonacci(n))