import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhập vào số n để in ra số Fibonacci thứ n: ");
        int n = scanner.nextInt();
        
        if (n <= 0) {
            System.out.println("Vui lòng nhập số nguyên dương.");
        } else {
            int result = fibonacci(n);
            System.out.println("Số Fibonacci thứ " + n + " là: " + result);
        }
        
        scanner.close();
    }

    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        
        int first = 0, second = 1, result = 0;
        for (int i = 2; i <= n; i++) {
            result = first + second;
            first = second;
            second = result;
        }
        
        return result;
    }
}

