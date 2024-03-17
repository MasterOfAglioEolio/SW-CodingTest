package test;

import java.util.*;

public class lotto {
    public static void main(String[] args) {

        ArrayList<Integer> lottoNumbers = new ArrayList<>();
        Random random= new Random();

        while(lottoNumbers.size()<6){
            int number = random.nextInt(45)+1;

            if(!lottoNumbers.contains(number)){
                lottoNumbers.add(number);
            }
        }

        Collections.sort(lottoNumbers);

        System.out.println(lottoNumbers);

    }
}
