import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner teclat = new Scanner(System.in);
        int files;
        int columnes;

        // 1.1. Demanar quantitat de files i quantitat de columnes
        System.out.print("Introdueix el nombre de files (imparell): ");
        files = teclat.nextInt();
        while (files % 2 == 0) {
            System.out.println("Error: El número ha de ser imparell.");
            files = teclat.nextInt();
        }
        System.out.print("Introdueix el nombre de columnes (imparell): ");
        columnes = teclat.nextInt();
        while (columnes % 2 == 0) {
            System.out.println("Error: El número ha de ser imparell.");
            columnes = teclat.nextInt();
        }
        int centreF = files / 2;
        int centreC = columnes / 2;


        // Per al tauler caldrà definir 2 matrius (de caràcters) paral·leles
        char[][] mPunts = new char[files][columnes];
        char[][] mFitxes = new char[files][columnes];

        // Posar els "colors" de les caselles

        // Aspes p diagonal
        for (int i = 0; i < files; i++) {
            for (int j = 0; j < columnes; j++) {
                mPunts[i][j] = ' '; // Posem un espai en blanc inicial
            }
        }
        int limit = (files < columnes) ? centreF : centreC;
        for (int i = 0; i <= limit; i++) {
            mPunts[centreF + i][centreC + i] = 'p';
            mPunts[centreF + i][centreC - i] = 'p';
            mPunts[centreF - i][centreC - i] = 'p';
            mPunts[centreF - i][centreC + i] = 'p';
        }
        // Cuadricula P (hardcoding)
        mPunts[0][0] = 'P';
        mPunts[0][centreC] = 'P';
        mPunts[0][columnes-1] = 'P';

        mPunts[centreF][0] = 'P';
        mPunts[centreF][columnes-1] = 'P';

        mPunts[files-1][0] = 'P';
        mPunts[files-1][centreC] = 'P';
        mPunts[files-1][columnes-1] = 'P';

        // Random 5 I

        for (int i = 0; i < 5; i++) {
            int numF;
            int numC;
            do {
                // Busquem dades dins del primer quadrant
                numF = (int)(Math.random()*centreF) + 1;
                numC = (int)(Math.random()*centreC) + 1;
            } while (mPunts[numF][numC] != ' ');
            // 1er quadrant
            mPunts[numF][numC] = 'I';
            // 3er quadrant
            mPunts[files - numF -1][numC] = 'I';
            // 4rt quadrant
            mPunts[files - numF -1][columnes - numC-1] = 'I';
            // 2n quadrant
            mPunts[numF][columnes - numC -1] = 'I';
        }
        // Patró GRID L
        for (int i = 2; i <= limit; i = i + 4) {
            for (int j = 2; j <= limit; j = j + 4) {
                mPunts[centreF + i][centreC + j] = 'L';
                mPunts[centreF + i][centreC - j] = 'L';
                mPunts[centreF - i][centreC + j] = 'L';
                mPunts[centreF - i][centreC - j] = 'L';
            }

        }

        // 1. Imprimir els números de les columnes
        System.out.print("   "); //
        for (int j = 0; j < columnes; j++) {       
            System.out.print(((j + 1) % 10) + " ");
        }
        System.out.println(); 
        for (int i = 0; i < files; i++) {
            System.out.print(((i + 1) % 10) + "  ");
            for (int j = 0; j < columnes; j++) {
                        System.out.print(mPunts[i][j] + " ");
            }
            System.out.println(); 
        }
    }
}