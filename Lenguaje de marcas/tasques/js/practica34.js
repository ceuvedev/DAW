"use strict";

// Definim la funció

function multiplicador(a, b) {
// Mostra el núm. inicial (b)
    console.log(b);
    // Faig un bucle amb el parametres donats. Repetim "a" voltes, cada volta multipliquem b * 2 e imprint
    for (let i = 1; i < a; i++) {
        b *= 2;
        console.log(b);
    }
}

// Invocació de la funció

multiplicador(6, 4);
