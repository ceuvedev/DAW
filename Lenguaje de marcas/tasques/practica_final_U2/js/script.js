"use strict";

document.addEventListener("DOMContentLoaded", () => {
    // Seleccionem els elements principals 
    const formulario = document.querySelector("#formulario");
    const mensaje = document.querySelector("#ola");

    formulario.addEventListener("submit", (event) => {
        // Evitem que la pàgina es recarregue 
        event.preventDefault();

       
        const nom = document.querySelector("#nombre").value;
        const email = document.querySelector("#email").value;
        const comentario = document.querySelector("#comentario").value;
        const condiciones = document.querySelector("#condiciones").checked;

        // 4. Validació 
        let error = "";

        if (nom === "") {
            error += "El nom és obligatori. ";
        }

        // Validació senzilla d'email (comprova @ i punt) 
        if (!email.includes("@") || !email.includes(".")) {
            error += "L'email no és vàlid. ";
        }

        if (comentario === "") {
            error += "Escriu un comentari. ";
        }

        if (!condiciones) {
            error += "Has d'acceptar les condicions. "; 
        }
        // Missatge
        if (error !== "") {
            // Si hi ha errors, es mostren en el DOM 
            mensaje.textContent = error;
        } else {
            mensaje.textContent = "Gràcies " + nom + ", hem rebut el teu missatge correctament.";
            formulario.reset();
        }
    });
});