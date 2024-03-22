package sort;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class study_1 {
    public static void main(String[] args) {
//        ArrayList<Integer> list=new ArrayList<>(Arrays.asList(15, 2, 3, 12, 64, 32, 14, 17, 5, 9));
//        Collections.sort(list,Collections.reverseOrder());
//        Collections.sort(list);
//        System.out.println(list);
        int[] data={15, 2, 3, 12, 64, 32, 14, 17, 5, 9};
//        bubble(data);
        selection(data);
//        insertion(data);
        System.out.println(Arrays.toString(data));
    }

    public static void bubble(int[] data){
        for(int i=0; i<data.length-1;i++){
            for(int j=0;j<data.length-i-1;j++){
                if(data[j+1]<data[j]){
                    int temp=data[j];
                    data[j]=data[j+1];
                    data[j+1]=temp;
                }
            }
        }
    }

    public static void selection(int[] data){
        for(int i=0;i<data.length-1;i++){
            int min=i;
            for(int j=i+1;j<data.length;j++){
                if(data[min]>data[j]){
                    min=j;
                }
            }
            int temp=data[min];
            data[min]=data[i];
            data[i]=temp;
        }
    }

    public static void insertion(int[] data){
        for(int i=0; i<data.length-1;i++){
            for(int j=i+1;j>0;j--){
                if(data[j]<data[j-1]){
                    int temp=data[j-1];
                    data[j-1]=data[j];
                    data[j]=temp;
                }
            }
        }
    }

}
