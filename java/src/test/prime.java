package test;

import java.util.ArrayList;
import java.util.Arrays;

public class prime {
    public static void main(String[] args) {
        // 100까지 소수 구하기
        int count=0;
        ArrayList<Integer> result=new ArrayList<>();

        for(int i=2;i<=100;i++){
            for(int j=2;j<=i;j++){
                if(i%j==0){
                    count++;
                }
            }
            if(count==1){
                result.add(i);
            }
            count=0;
        }
        System.out.println(result);

    }
}
