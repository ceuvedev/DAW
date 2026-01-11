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
        int centroF = files / 2;
        int centroC = columnes / 2;


        // 1.2. Per al tauler caldrà definir 2 matrius (de caràcters) paral·leles
        char[][] mPunts = new char[files][columnes];
        char[][] mFitxes = new char[files][columnes];

        //1.3 Posar els "colors" de les caselles
        for (int i = 0; i < files; i++) {
            for (int j = 0; j < columnes; j++) {
                mPunts[i][j] = ' '; // Posem un espai en blanc inicial
            }
        }
        int limit = (files < columnes) ? centroF : centroC;
        for (int i = 0; i <= limit; i++) {
            mPunts[centroF + i][centroC + i] = 'p';
            mPunts[centroF + i][centroC - i] = 'p';
            mPunts[centroF - i][centroC - i] = 'p';
            mPunts[centroF - i][centroC + i] = 'p';
        }




        // Ara ja podries començar a posar les lletres 'p', 'P', 'l', etc.
        // 1. Imprimir números de columnas (cabecera)
        System.out.print("   "); // Espacio inicial para compensar el número de fila
        for (int j = 0; j < columnes; j++) {
            System.out.print((j + 1) + " ");
        }
        System.out.println(); // Salto de línea tras la cabecera

        // 2. Recorrer la matriz para imprimir filas y contenido
        for (int i = 0; i < files; i++) {
            // Imprimir el número de fila (coordenada)
            System.out.print((i + 1) + "  ");

            for (int j = 0; j < columnes; j++) {
                // Imprimir el contenido de la celda seguido de un espacio
                System.out.print(mPunts[i][j] + " ");
            }
            System.out.println(); // Salto de línea al terminar cada fila
        }
    }
}