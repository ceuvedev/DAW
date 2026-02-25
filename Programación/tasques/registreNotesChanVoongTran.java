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
                    notaAlumne();
                    break;
                case 3:
                    buscarAlumne(alu);
                    break;
                case 4:
                    modificarAlumne(alu);
                    break;
                case 5:
                    modificarNota();
                    break;
                case 6:
                    borrarAlumne(alu);
                    break;
                case 7:
                    wipe(alu);
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

    /*(1) Demanarà les dades personals d'un alumne (no les notes) i les guardarà.
    Caldrà buscar una posició lliure del vector on posar l’alumne */
    static void altaAlumne (Alumne[] alu){
        for(int i=0; i < alu.length; i++ ) {
            if (alu[i].nom.equals("")){
                alu[i].nom = funcionsIO.readTextC("Dime el teu nom: ");
                alu[i].tlf = funcionsIO.readIntC("Dime el teu telf: ");
                alu[i].adre.carrer = funcionsIO.readTextC("Dime el teu carrer: ");
                break;
            }
        }

    }

    /* (2) Preguntarà quina avaluació i assignatura i anirà demanant per teclat les notes
    corresponents de cada alumne donat d'alta (anirà mostrant el nom) i guardarà
    eixes notes.*/
    static void notaAlumne (){
        //bucle niuat?
        System.out.println("La teua nota: ");
    }

    /*(3) Preguntarà pel nom de l’alumne i mostrarà totes les seues dades. S’imagina
    que els alumnes tenen tots un nom diferent.*/
    static void buscarAlumne (Alumne[] alu){
        System.out.println("A quí busques? Indicam el nom: ");
        String buscarNom = funcionsIO.readTextC("Dime el nom a buscar: ");
        for (int i = 0; i<alu.length; i++) {
            if (alu[i].nom.equalsIgnoreCase(buscarNom)) {
                System.out.println("Te encontre");
                System.out.println("eres: " + alu[i].nom);
                System.out.println("vives: " + alu[i].adre.carrer);
                System.out.println("Tu telf es: " + alu[i].tlf);
            } else {
                System.out.println("No trobat :(");
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

    static void modificarNota (){
        System.out.println("S'ha modificat la nota");
    }
    /*(6) Pregunta el nom d'un alumne, mostrarà les seues dades, preguntarà si està
    segur d'esborrar i, si és així, l'esborrarà de la llista.*/

    static void borrarAlumne (Alumne[] alu){

        System.out.println("A quí vols modificar Indicam el nom: ");
        String buscarNom = funcionsIO.readTextC("Dime el nom a buscar: ");
        for (int i = 0; i<alu.length; i++) {
            if (alu[i].nom.equalsIgnoreCase(buscarNom)) {
                alu[i].nom = "";
            }
        }System.out.println("Alumne esborrat");
    }
    /* (7) Pregunta si està segur i, si és així, esborrarà tota la llista.*/

    static void wipe (Alumne[] alu){

        for (int i = 0; i<alu.length; i++) {
            alu[i].nom = "";
        }
        System.out.println("S'ha borrar totes les dades");
    }
    /**/

    static void estadistiques(){
        System.out.println("Adios");
    }
}
