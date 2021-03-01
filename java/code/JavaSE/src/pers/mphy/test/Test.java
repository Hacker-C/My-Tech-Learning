package pers.mphy.test;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        final double PI = 3.14159;
        double radious = input.nextDouble();
        double ans = PI * Math.pow(radious, 2);
        System.out.println("The answer is " + ans);
    }
}

