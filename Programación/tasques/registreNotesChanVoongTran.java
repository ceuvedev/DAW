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
        final int N = 100;
        Alumne alu[] = new Alumne[N];
        for (int i=0; i<N; i++) {
            alu[i] = new Alumne();
            alu[i].nom = "";
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
            System.out.println("Tria una opció: ");

            opcio = funcionsIO.readIntC("Per favor, indica un num 1-8 o 0 per a ixir");


            switch (opcio) {
                case 1:
                    altaAlumne(alu);
                    break;
                case 2:
                    notaAlumne(alu);
                    break;
                case 3:
                    buscarAlumne(alu);
                    break;
                case 4:
                    modificarAlumne(alu);
                    break;
                case 5:
                    modificarNota(alu);
                    break;
                case 6:
                    borrarAlumne(alu);
                    break;
                case 7:
                    wipe(alu);
                    break;
                case 8:
                    estadistiques(alu);
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

    /*(1) Demanarà les dades personals d'un alumne (no les notes) i les guardarà.
    Caldrà buscar una posició lliure del vector on posar l’alumne */
    static void altaAlumne (Alumne[] alu){
        for(int i=0; i < alu.length; i++ ) {
            if (alu[i].nom.equalsIgnoreCase("")){
                alu[i].nom = funcionsIO.readTextC("Dime el teu nom: ");
                alu[i].tlf = funcionsIO.readIntC("Dime el teu telf: ");
                alu[i].adre.carrer = funcionsIO.readTextC("Dime el teu carrer: ");
                break;
            }
        }
        System.out.println("Está tot plé!");
    }
    /* (2) Preguntarà quina avaluació i assignatura i anirà demanant per teclat les notes
    corresponents de cada alumne donat d'alta (anirà mostrant el nom) i guardarà
    eixes notes.*/
    static void notaAlumne (Alumne[] alu){
        //Fiquem dos nous variables per a treballar el array notas[assignatura(fila)][avaluacio(columna)]
        int aval = funcionsIO.readIntC("Dis-me la avaluació: (1, 2, 3)");
        int assignatura = funcionsIO.readIntC("Dis-me la assignatura: (1: PRG, 2: BDA, 3: EDD)");
        for (int i=0; i < alu.length; i++) {
            //el bucle tria només als alumnes amb valors i executa el bloc de codi
            if (!alu[i].nom.equalsIgnoreCase("")) {
                System.out.println("Alumno: " + alu[i].nom);
                //Com el array comença per index 0, reste -1 per a que en el input sea human friendly
                alu[i].notas[assignatura-1][aval-1] = funcionsIO.readDoubleC("Dis-me la nota: ");
            }
        }
    }
    /*(3) Preguntarà pel nom de l’alumne i mostrarà totes les seues dades. S’imagina
    que els alumnes tenen tots un nom diferent.*/
    static void buscarAlumne (Alumne[] alu){
        String buscarNom = funcionsIO.readTextC("Dime el nom a buscar: ");
        for (int i = 0; i<alu.length; i++) {
            if (alu[i].nom.equalsIgnoreCase(buscarNom)) {
                System.out.println("Te encontre");
                System.out.println("eres: " + alu[i].nom);
                System.out.println("vives: " + alu[i].adre.carrer);
                System.out.println("Tu telf es: " + alu[i].tlf);
            }
        }
    }
    /*(4) Pregunta el nom d'un alumne, mostrarà les seues dades, demanarà les noves
    dades a modificar (nom, telèfon i adreça) i modificarà eixe alumne en la llista.*/

    static void modificarAlumne (Alumne[] alu){
        System.out.println("A quí vols modificar Indicam el nom: ");
        String buscarNom = funcionsIO.readTextC("Dime el nom a buscar: ");
        for (int i = 0; i<alu.length; i++) {
            if (alu[i].nom.equalsIgnoreCase(buscarNom)) {
                alu[i].nom = funcionsIO.readTextC("Com et diuen? ");
                alu[i].adre.carrer = funcionsIO.readTextC("Quín carrer vius ara? ");
                alu[i].tlf = funcionsIO.readIntC("Quín telf. tens ara? ");
            }
        }
        System.out.println("S'ha modificat l'alumne");
    }
    /*(5) Pregunta el nom d'un alumne, mostrarà les seues dades, preguntarà quina
    assignatura i quina avaluació, quina nota i la modificarà.*/

    static void modificarNota (Alumne[] alu){
        String buscarNom = funcionsIO.readTextC("Dime el nom a buscar: ");
        for (int i = 0; i<alu.length; i++) {
            if (alu[i].nom.equalsIgnoreCase(buscarNom)) {
                int aval = funcionsIO.readIntC("Dis-me la avaluació: (1, 2, 3)");
                int assignatura = funcionsIO.readIntC("Dis-me la assignatura: (1: PRG, 2: BDA, 3: EDD)");
                    //Com el array comença per index 0, reste -1 per a que en el input sea human friendly
                    alu[i].notas[assignatura - 1][aval - 1] = funcionsIO.readDoubleC("Dis-me la nota: ");
                    System.out.println("S'ha modificat la nota");
            }
        }
    }
    /*(6) Pregunta el nom d'un alumne, mostrarà les seues dades, preguntarà si està
    segur d'esborrar i, si és així, l'esborrarà de la llista.*/
    static void borrarAlumne (Alumne[] alu){
        System.out.println("A quí vols modificar Indicam el nom: ");
        String buscarNom = funcionsIO.readTextC("Dime el nom a buscar: ");
        for (int i = 0; i<alu.length; i++) {
            // la logica es que si el nom coincideix, sobre-escriu només el nom de alu en eixe index.
            if (alu[i].nom.equalsIgnoreCase(buscarNom)) {
                alu[i].nom = "";
            }
        }System.out.println("Alumne esborrat");
    }
    /* (7) Pregunta si està segur i, si és així, esborrarà tota la llista.*/

    static void wipe (Alumne[] alu){
        int trigger = 0;
        trigger = funcionsIO.readIntC("Vols borrar tots els dades? 0: No 1: Sí ");
        // Si la condició es verdader, s'executa el bloc
        if (trigger == 1) {
            for (int i = 0; i<alu.length; i++) {
                alu[i].nom = "";
            }
            System.out.println("S'ha borrar totes les dades");
        } else {
            System.out.println("No s'ha borrar les dades");
        }
    }
    /*(8) Mostrarà els percentatges d'aprovats*/

    static void estadistiques(Alumne[] alu){
        String assignaturas[] = {"PRG\t", "BDA\t", "EDD\t", "Total"};
        String aval[] = {" ", "AV1", "AV2", "AV3", "Total"};
        System.out.println("\t\t AV1\t AV2\t AV3\t TOTAL");
        for(int fil = 0; fil < 4; fil++) {
            System.out.print(assignaturas[fil] + "\t");
            for (int col = 0; col < 5; col++) {
                System.out.print(aval[col] + "\t");
            }
            System.out.println();
        }
    }
}
