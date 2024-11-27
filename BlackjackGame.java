import java.util.ArrayList;
import java.util.Scanner;
import java.util.List;

public class BlackjackGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Dice dice = new Dice();

        // Skapa spelare
        boolean playerJoin = true;
        List<Player> playersList = new ArrayList<>();
        int playerId = 1;

        while (playerJoin) {
            System.out.println("Ny spelare? (ja/nej)");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("ja")) {
                Player player = new Player("Spelare[" + playerId +"]");
                playersList.add(player);
                System.out.println("Lagt till " + player.name);
                playerId++;
            } else {
                playerJoin = false;
            }
        }

        Player computer = new Player("Datorn");

        System.out.println("Välkommen till Blackjack med tärningar!");
        System.out.println("Målet är att komma så nära 21 som möjligt utan att överstiga det.\n");

        // Huvudspel-loop
        while (true) {

            playersList.forEach(player -> {
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
            });

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
            boolean allPlayersStanding = playersList.stream().allMatch(Player::isStanding);
            if (allPlayersStanding && computer.isStanding()) {
                System.out.println("\nBåda har stannat. Slutresultat:");
                playersList.forEach(player -> {
                    System.out.println(player.getName() + ": " + player.getScore());
                });
                System.out.println(computer.getName() + ": " + computer.getScore());

                for (Player player : playersList) {
                    if (player.getScore() > computer.getScore()) {
                        System.out.println(player.getName() + " vinner!");
                    } else if (player.getScore() < computer.getScore()) {
                        System.out.println("Datorn vinner!");
                    } else {
                        System.out.println("Det är oavgjort!");
                    }
                }
                return;
            }
        }
    }
}