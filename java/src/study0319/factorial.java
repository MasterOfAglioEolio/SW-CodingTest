package study0319;

public class factorial {
    static int[] cache=new int[10];
    public static void main(String[] args) {
        System.out.println(recur_factorial(6));
        System.out.println(mem_factorial(6));
    }

    public static int recur_factorial(int data){
        if(data<=1){
            return 1;
        }
        else{
            return data*recur_factorial(data-1);
        }
    }
    public static int mem_factorial(int data){
        if(data<=1){
            cache[data]=1;
            return 1;
        }
        else{
            cache[data]=data*mem_factorial(data-1);
            return cache[data];
        }
    }
}
