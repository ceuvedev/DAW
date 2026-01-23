"use strict";

// Definim la funció

function multiplicador(a, b) {
    console.log(b);
    for (let i = 0; i < a -1; i++) {
        b *= 2;
        console.log(b);
    }
}

// Invocació de la funció

multiplicador(6, 4);