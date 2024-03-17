package sort;

import java.util.Arrays;

public class selection {
    public static void main(String[] args) {
        int[] list = {15, 2, 3, 12, 64, 32, 14, 17, 5, 9};

        for(int i=0;i<list.length-1;i++){
            int min_idx=i;
            for(int j=i+1;j<list.length;j++){
                if(list[j]<list[min_idx]){
                    min_idx=j;

                }
            }
            int temp=list[min_idx];
            list[min_idx]=list[i];
            list[i]=temp;
        }
        System.out.println(Arrays.toString(list));

    }
}
