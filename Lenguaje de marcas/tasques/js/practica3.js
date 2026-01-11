"use strict";

function calcularNumero(num) {
    // aquí se hace el control de "tipo"
    if (typeof num !== 'number' || Number.isNaN(num)) {
        return console.log('No es un número válido ');
    }
    // esta parte hace la logica con if e else if
    if (num > 0) {
        console.log(`El número ${num} es positivo. `);
    } else if (num < 0) {
        console.log(`El número ${num} es negativo. `);
    } else {
        console.log(`El número es cero. `);
    }
}

// pruebas con distintos inputs
calcularNumero(10);
calcularNumero('hola');
calcularNumero(-10);
calcularNumero(0);