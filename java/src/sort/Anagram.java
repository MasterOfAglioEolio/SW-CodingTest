package sort;

import java.util.Arrays;

public class Anagram {
    public static void main(String[] args) {
        String an1="acdbe";
        String an2="ebdqa";
        String num="12345";
        System.out.println(num);
        Integer s_num=Integer.valueOf(num);
        System.out.println(s_num);
        char[] a=an1.toCharArray();
        char[] b=an2.toCharArray();

        Arrays.sort(a);
        Arrays.sort(b);
        if(Arrays.equals(a,b)){
            System.out.println("ana");
        }
        else{
            System.out.println("dif");
        }

    }
}
