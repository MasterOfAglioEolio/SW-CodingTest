package study0319;

import java.util.ArrayList;

public class parseInt {
    //Integer.parseInt() 두번째 매개변수가 생략된 경우 10진수로 변환된 값을 반환하고,
    //Integer.parseInt() 10진수가 아닌 다른 진수로 변환하고 싶으면 두 번째 매개변수에 변환하고자 하는 진수를 입력합니다.

    //valueOf() 메서드는 파라미터로 숫자로 변환할 문자열을 입력받고, 참조형인 new Integer(정수)로 변환합니다.
    //valueOf() 메서드는 문자열의 값을 정수형(int)로 변환한 다음 Integer Object(객체)로 만들어서 반환합니다.


    public static void main(String[] args) {
        String str="123456";
        int result1=Integer.parseInt(str);
        int result2=Integer.valueOf(str);
        System.out.println(result1);
        System.out.println(result2);
        String result3=String.valueOf(result1);
        System.out.println(result3);
    }


}
