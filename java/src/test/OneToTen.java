package test;

import java.util.ArrayList;
import java.util.Random;

public class OneToTen {
    public static void main(String[] args) {
        ArrayList<Integer> arrayList=new ArrayList<>();
        Random random=new Random();

        for(int i=0;i<10;i++){
            int number=random.nextInt(10)+1;
            if(arrayList.contains(number))
            {
                System.out.println("true");
                break;
            }
            else {

                arrayList.add(number);
            }
        }
        System.out.println(arrayList);



    }
}
