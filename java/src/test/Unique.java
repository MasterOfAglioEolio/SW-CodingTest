package test;

import java.util.HashSet;

public class Unique {
    public static boolean isUnique(String str) {
        HashSet<Integer> hs=new HashSet<>();
        char[] arr=str.toCharArray();

        for(int c :arr){
            if(hs.contains(c)){
                return false;
            }
            hs.add(c);
        }
        return true;
    }

    public static void main(String[] args) {
        String testStr="1233345";
        System.out.println(isUnique(testStr));
    }
}
