"use strict";

// Definim la funció amb dades per defecte

function producte(nom = "Producte", preu, impost = 10) {
    // Lógica de control  (convertir els valors al tipus adequat i comprovar el preu que siguen valits)
    if (isNaN(preu) || preu < 0) {
        console.error("Error: El preu ha de ser un número positiu.");
        return;
    }
    if (isNaN(impost) || impost < 0) {
        console.error("Error: El preu ha de ser un número positiu.");
        return;
    }

    // Imprimim 
    let preuFinal = preu + (preu * (impost / 100));
    console.log(`Producte: ${nom}`);
    console.log(`Preu: ${preu} €`);
    console.log(`Impost: ${impost} %`);
    console.log(`Preu final: ${preuFinal} €`);    
}

// Crida la funció diverses vegades amb diferents valors.

producte(); // prova forçant valor per defecte
producte("Ratoli", 20, ); // forçant el impost per defecte
producte("Teclat",-2 , 21); // forçant el preu negatiu
producte("Monitor", 150, 21); // prova amb tots els valors