class Adresa{
    String carrer;
    int num;
    int CP;
}

class Alumne {
    String nom;
    int tlf;
    Adresa adre = new Adresa();
    double[][] notas = new double[3][3];
}

public class registreNotesChanVoongTran {

    public static void main(String[] args) {
        final int N = 3;
        Alumne alu[] = new Alumne[N];
        for (int i=0; i<N; i++) {
            alu[i] = new Alumne();
        }

        int opcio;
        do {
            //
            System.out.println("\n--- MENÚ registreNotes ---");
            System.out.println("1. Alta alumne");
            System.out.println("2. Posar nota alumnes");
            System.out.println("3. Buscar alumne");
            System.out.println("4. Modificar dades alumne");
            System.out.println("5. Modificar nota d'alumne");
            System.out.println("6. Esborrar un alumne");
            System.out.println("7. Esborrar tots els alumnes");
            System.out.println("8. Estadistiques");
            System.out.println("0. Sortir del programa");
            System.out.print("Tria una opció: ");

            opcio = funcionsIO.readIntC("Indica una opció");


            switch (opcio) {
                case 1:
                    altaAlumne();
                    break;
                case 2:
                    notaAlumne();
                    break;
                case 3:
                    buscarAlumne();
                    break;
                case 4:
                    modificarAlumne();
                    break;
                case 5:
                    modificarNota();
                    break;
                case 6:
                    borrarAlumne();
                    break;
                case 7:
                    wipe();
                    break;
                case 8:
                    estadistiques();
                    break;
                case 0:
                    System.out.println("Adeu");
                    break;
                default:
                    System.out.println("Error: Opció no vàlida. Torna-ho a provar.");
            }

            // 3. El bucle continua MENTRE l'opció siga diferent de 0
        } while (opcio != 0);
        System.out.println("Indica una opció correcta: ");

    }

    // Definin els metodos
    static void altaAlumne (){






    }
    static void notaAlumne (){
        System.out.println("Adios");
    }
    static void buscarAlumne (){
        System.out.println("A quí busques? Indicam el nom: ");
        for (int i = 0; i<N; i++) {

        }

        System.out.println("Adios");
    }
    static void modificarAlumne (){
        System.out.println("S'ha modificat l'alumne");
    }
    static void modificarNota (){
        System.out.println("S'ha modificat la nota");
    }
    static void borrarAlumne (){
        System.out.println("Alumne esborrat");
    }
    static void wipe (){
        System.out.println("S'ha borrar totes les dades");
    }
    static void estadistiques(){
        System.out.println("Adios");
    }
}
