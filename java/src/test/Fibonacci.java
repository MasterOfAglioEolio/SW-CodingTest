package test;

public class Fibonacci {
    static int[] cache = new int[11];

    public static void main(String[] args){
        System.out.println(loopFibonacci(8));
        System.out.println(recurFibonacci(8));
        System.out.println(dpFibonacci(8));
    }

    public static int loopFibonacci(int n){
        int a=0, b=1, c=0;

        if(n==0){
            return 0;
        }
        else if(n==1){
            return 1;
        }
        else{
            for (int i=2;i<=n;i++){
                c=a+b;
                a=b;
                b=c;
            }
        }
        return c;
    }

    public static int recurFibonacci(int n){
        if(n==0){
            return 0;
        }
        if(n==1){
            return 1;
        }

        return recurFibonacci(n-1)+recurFibonacci(n-2);
    }

    public static int dpFibonacci(int n){
        if(n==0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        int ret = cache[n];
        if(ret != 0 )
        {
            return ret;
        }

        return cache[n] = dpFibonacci(n-1)+dpFibonacci(n-2);
    }

}
