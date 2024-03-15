package test;

import java.util.Arrays;

public class Anagram {
    public static void main(String[] args){
        char[] a = "acdbe".toCharArray();
        char[] b = "ecabd".toCharArray();
        System.out.println(a);
        Arrays.sort(a);
        Arrays.sort(b);

        if(Arrays.equals(a,b)){
            System.out.println(true);
            System.out.println(a);
        }
        else{
            System.out.println(false);
        }
    }
}
