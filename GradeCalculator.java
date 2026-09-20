import java.util.Scanner;

public class GradeCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (true) {
            System.out.print("Java Score: ");
            double javaScore = input.nextDouble();

            System.out.print("C Score: ");
            double cScore = input.nextDouble();

            System.out.print("Database Handling Score: ");
            double databaseScore = input.nextDouble();

            double average = (javaScore + cScore + databaseScore) / 3;
            char grade;

            if (average >= 90 && average <= 100) {
                grade = 'A';
            } else if (average >= 80) {
                grade = 'B';
            } else if (average >= 75) {
                grade = 'C';
            } else {
                grade = 'F';
            }

            System.out.printf("Average: %.3f%n", average);
            System.out.println("Grade: " + grade);

            System.out.print("Do you want to continue? YES / NO: ");
            String choice = input.next();

            switch (choice.toUpperCase()) {
                case "YES":
                    break;

                case "NO":
                    input.close();
                    return;

                default:
                    System.out.println("Invalid choice. Program terminated.");
                    input.close();
                    return;
            }
        }
    }
}