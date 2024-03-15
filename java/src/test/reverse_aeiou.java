package test;

import java.util.HashSet;

public class reverse_aeiou {
    public static void main(String[] args) {
        String str = "bacedufivo";
        StringBuilder sb = new StringBuilder(str);
        HashSet<Character> vowel = new HashSet<>();
        vowel.add('a');
        vowel.add('e');
        vowel.add('i');
        vowel.add('o');
        vowel.add('u');

        int left = 0, right = str.length() - 1;

        while(left < right) {
            while(!vowel.contains(str.charAt(left)))
                left++;
            while(!vowel.contains(str.charAt(right)))
                right--;

            sb.setCharAt(left, str.charAt(right));
            sb.setCharAt(right, str.charAt(left));

            left++;
            right--;
        }

        System.out.println(sb);
    }

}
