package sort;

import java.util.ArrayList;
import java.util.Scanner;

public class SN {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int num=sc.nextInt();
        ArrayList<Integer> result=new ArrayList<>();
        for(int i=2;i<=num;i++){
            int count=0;
            for(int j=2;j<=num;j++){
                if(i%j==0){
                    count++;
                }
            }
            if(count==1){
                result.add(i);
            }
        }
        System.out.println(result);
    }
}
