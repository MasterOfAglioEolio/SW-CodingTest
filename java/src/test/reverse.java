package test;

public class reverse {
    public static void main(String[] args) {
        String str="asdqwez";
        char[] arr=str.toCharArray();
        char[] result=new char[str.length()];
        System.out.println(arr);
        for(int i=str.length()-1;i>=0;i--){
            result[str.length()-1-i]=arr[i];
        }
        System.out.println(result);
    }

    public static void main2(String[] args) {
        String str="asdqwez";
        StringBuilder sb = new StringBuilder();
        sb.reverse();
        System.out.println(sb);
    }
}
