package study0319;

public class fibo {
    static int[] cache=new int[10];
    public static void main(String[] args) {
        System.out.println(fibo(9));
        System.out.println(recur_fibo(9));

    }
    public static int fibo(int data){
        if(data<=1){
            cache[data]=1;
            return 1;
        }

        return cache[data]=fibo(data-1)+fibo(data-2);
    }

    public static int recur_fibo(int data){
        if(data<=1){
            return 1;
        }
        else{
            return recur_fibo(data-1)+recur_fibo(data-2);
        }
    }
}
