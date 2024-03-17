package sort;

import java.util.Arrays;

public class bubble {
    public static void main(String[] args) {
        int[] list = {15, 2, 3, 12, 64, 32, 14, 17, 5, 9};

        for(int i=0;i<list.length-1;i++){
            for (int j=0;j<list.length-1;j++){
                if(list[j]>list[j+1]){
                    int temp=list[j];
                    list[j]=list[j+1];
                    list[j+1]=temp;

                }
            }
        }

        System.out.println(Arrays.toString(list));
    }
}
