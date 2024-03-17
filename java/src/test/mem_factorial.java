package test;

public class mem_factorial {
    public static int[] table;

    public static void main(String[] args) {
        table=new int[10];
        System.out.println(factorial(5));
    }

    public static int factorial(int data){
        if(data==1){
            table[data]=1;
        }
        if (table[data]>0){
            return table[data];
        }
        table[data]=data*factorial(data-1);
        return table[data];

    }
}
