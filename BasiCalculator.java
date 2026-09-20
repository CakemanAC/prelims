import java.util.Scanner;

public class BasiCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double x, y, result = 0.0;
        int choice;

        System.out.print("Enter value of x: ");
        x = input.nextDouble();

        System.out.print("Enter value of y: ");
        y = input.nextDouble();

        System.out.println("\nVariable values:");
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("result = " + result);

        System.out.println("\nArithmetic Operation:");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");
        System.out.println("5. Modulus");
        System.out.println("6. Increment");
        System.out.println("7. Decrement");

        System.out.print("Choose an operation: ");
        choice = input.nextInt();

        switch (choice) {
            case 1:
                result = x + y;
                System.out.println("Addition: x + y = " + result);
                break;

            case 2:
                result = x - y;
                System.out.println("Subtraction: x - y = " + result);
                break;

            case 3:
                result = x * y;
                System.out.println("Multiplication: x * y = " + result);
                break;

            case 4:
                if (y != 0) {
                    result = x / y;
                    System.out.println("Division: x / y = " + result);
                } else {
                    System.out.println("Division cannot be performed by zero.");
                }
                break;

            case 5:
                if (y != 0) {
                    result = x % y;
                    System.out.println("Modulus: x % y = " + result);
                } else {
                    System.out.println("Modulus cannot be performed by zero.");
                }
                break;

            case 6:
                x++;
                System.out.println("Increment: x++ = " + x);
                break;

            case 7:
                x--;
                System.out.println("Decrement: x-- = " + x);
                break;

            default:
                System.out.println("Invalid operation.");
        }

        input.close();
    }
}