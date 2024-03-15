package test;

public class Factorial {
    static int[] cache = new int[10];

    public static void main(String[] args) {
        System.out.println(loopFactorial(8));
        System.out.println(recurFactorial(8));
        System.out.println(dpFactorial(8));
    }

    public static int loopFactorial(int n){
        int result=1;
        for(int i=1; i<=n; i++){
            result*=i;
        }
        return result;
    }

    public static int recurFactorial(int n){
        if(n==1){
            return 1;
        }
        return n*recurFactorial(n-1);
    }

    public static int dpFactorial(int n){
        if(n==1){
            return 1;
        }
        int result=cache[n];

        if(result!=0){
            return result;
        }

        return cache[n]=n*dpFactorial(n-1);

    }
}
