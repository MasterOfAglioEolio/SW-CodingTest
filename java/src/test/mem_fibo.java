package test;

public class mem_fibo {
    public static int[] table;
    public static void main(String[] args) {

        table=new int[8];
        System.out.println(fibo(7));

    }
    public static int fibo(int data){
        if (data<=1){
            table[data]=1;
            return 1;
        }
        table[data]=fibo(data-1)+fibo(data-2);
        return table[data];
    }
}
