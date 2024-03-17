package sort;

import java.util.Arrays;

public class insertion {
    public static void main(String[] args) {
        int[] list = {15, 2, 3, 12, 64, 32, 14, 17, 5, 9};

        for(int i = 1; i<list.length;i++){
            for(int j=list.length-1; j>0;j--){
                if(list[j]<list[j-1]){
                    int temp=list[j];
                    list[j]=list[j-1];
                    list[j-1]=temp;
                }
            }
        }
        System.out.println(Arrays.toString(list));
    }


}
