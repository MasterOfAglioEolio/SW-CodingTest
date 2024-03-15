package test;



public class QuickSelection {
    static int K=4;
    static int ret = -1;

    public static void main(String[] args) {
        int[] arr={3,5,2,4,1};

        QuickSelection(arr,0,arr.length-1);
        System.out.println(ret);
    }
    public static void QuickSelection(int[] arr, int left, int right){
        int pivot =partition(arr,left,right);

        if(pivot==K-1){
            ret=arr[pivot];
        }
        else if(pivot>K-1){
            QuickSelection(arr,left,pivot-1);
        }
        else{
            QuickSelection(arr,pivot+1,right);
        }

    }
    public static int partition(int[] arr, int left, int right){
        int mid=(left+right)/2;
        swap(arr,left,right);

        int i = left, j=right;
        int pivot = arr[left];

        while(i<j){
            while(arr[j]>=pivot)
            {
                j--;
            }
            while(i<j && arr[i]<pivot){
                i++;
            }

            swap(arr,i,j);
        }
        arr[left]=arr[i];
        arr[i]=pivot;

        return i;
    }

    public static void swap(int[] arr, int a, int b){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
}
