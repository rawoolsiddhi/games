import java.util.*;

class GuessingGame {
    public static void main(String[] args) {
        int num = (int) (Math.random() * 100);
        System.out.println("Welcome to the Number Guessing Game!");
        System.out.println("Try to guess the number between 1 and 100.");

        try (Scanner obj = new Scanner(System.in)) {
            int attempts = 0;
            int guessNumber;

            do {
                System.out.print("Enter your guess (or -1 to quit): ");
                try {
                    guessNumber = obj.nextInt();
                } catch (InputMismatchException e) {
                    System.out.println("Invalid input. Please enter a number.");
                    obj.next(); // Consume the invalid input
                    continue;
                }

                if (guessNumber == -1) {
                    System.out.println("The number was: " + num);
                    break;
                } else if (num == guessNumber) {
                    System.out.println("Congratulations! You won!");
                    break;
                } else if (num > guessNumber) {
                    System.out.println("The guessed number is smaller.");
                } else {
                    System.out.println("The guessed number is bigger.");
                }

                attempts++;
            } while (true);

            System.out.println("Number of attempts: " + attempts);
        }
    }
}
