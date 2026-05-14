"use strict";

document.addEventListener("DOMContentLoaded", () =>{
    const formulario = document.getElementById("form");
    const mensaje = document.getElementById("mensaje");

    formulario.addEventListener("submit", (event)=>{
        event.preventDefault();

        const nom = document.getElementById("nom").value;
        const email = document.getElementById("nom").value;
        const comentario = document.getElementById("nom").value;
        const checkbox = document.getElementById("nom").checked;


        let error = "";

        if (nom === "") {
            error += "Falta possar el nom. ";
        }
        if (!email.includes("@") || !email.includes(".")) {
            error += "Falta possar el email. "
        }
        if (comentario === "") {
            error += "Falta possar un comentari. ";
        }
        if (!checkbox) {
            error += "Acepta condicions, per favor. "
        }
        if (error !== "") {
            mensaje.textContent = error;
        } else {
            mensaje.textContent = `Gràcies ${nom}, hem rebut el missatge correctament`

            formulario.reset();
        }

    });
}); 