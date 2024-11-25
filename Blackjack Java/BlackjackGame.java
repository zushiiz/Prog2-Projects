import java.util.Scanner;

public class BlackjackGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Dice dice = new Dice();

        // Skapa spelare
        Player player = new Player("Spelaren");
        Player computer = new Player("Datorn");

        System.out.println("Välkommen till Blackjack med tärningar!");
        System.out.println("Målet är att komma så nära 21 som möjligt utan att överstiga det.\n");

        // Huvudspel-loop
        while (true) {
            // Spelarens tur
            if (!player.isStanding()) {
                System.out.println(player.getName() + ", din poäng är: " + player.getScore());
                System.out.print("Vill du slå en tärning? (ja/nej): ");
                String choice = scanner.nextLine();

                if (choice.equalsIgnoreCase("ja")) {
                    int roll = dice.roll();
                    System.out.println("Du slog: " + roll);
                    player.addScore(roll);

                    if (player.getScore() > 21) {
                        System.out.println("Du har överstigit 21! Du förlorar.");
                        return;
                    }
                } else {
                    player.stand();
                }
            }

            // Datorns tur
            if (!computer.isStanding()) {
                System.out.println("\n" + computer.getName() + " tänker...");
                if (computer.getScore() < 17) {
                    int roll = dice.roll();
                    System.out.println(computer.getName() + " slog: " + roll);
                    computer.addScore(roll);

                    if (computer.getScore() > 21) {
                        System.out.println(computer.getName() + " har överstigit 21! Du vinner!");
                        return;
                    }
                } else {
                    computer.stand();
                    System.out.println(computer.getName() + " stannar.");
                }
            }

            // Kontrollera om båda har stannat
            if (player.isStanding() && computer.isStanding()) {
                System.out.println("\nBåda har stannat. Slutresultat:");
                System.out.println(player.getName() + ": " + player.getScore());
                System.out.println(computer.getName() + ": " + computer.getScore());

                if (player.getScore() > computer.getScore()) {
                    System.out.println("Du vinner!");
                } else if (player.getScore() < computer.getScore()) {
                    System.out.println("Datorn vinner!");
                } else {
                    System.out.println("Det är oavgjort!");
                }
                return;
            }
        }
    }
}