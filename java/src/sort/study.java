package sort;

import java.util.ArrayList;
import java.util.Arrays;

public class study {
    public static void main(String[] args){
        int[] list = {15, 2, 3, 12, 64, 32, 14, 17, 5, 9};
//        bubble(list);
//        selection(list);
        insertion(list);
        for(int li:list){
            System.out.print(li+" ");

        }
    }

    public static void bubble(int[] data){

        for(int i=0;i<data.length-1;i++){
            for (int j=0;j<data.length-1-i;j++){ //이전에 정렬된 것들은 넘어가고
                if(data[j]>data[j+1]){
                    int temp=data[j+1];
                    data[j+1]=data[j];
                    data[j]=temp;
                }
            }
        }

    }

    public static void selection(int[] data){
        int min_idx=0;
        for(int i=0;i<data.length-1;i++){
            min_idx=i;
            for(int j=i+1;j<data.length;j++){
                if(data[j]<data[min_idx]){
                    min_idx=j;
                }
            }
            int temp=data[min_idx];
            data[min_idx]=data[i];
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
