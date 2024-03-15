package test;

// 유클리드 호제법
// 최소공배수 = (n1 * n2) / (n1과 n2의 최대공약수)
public class GCD_LCM {
    public static void main(String[] args){
        System.out.println(gcd(8,12));

        int LCM=(8*12)/gcd(8,12);
        System.out.println(LCM);

    }
    public static int gcd(int a, int b){
        if(b==0){
            return a;
        }
        else{
            return gcd(b, a%b);
        }
    }
}
