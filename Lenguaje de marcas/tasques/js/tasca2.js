
document.addEventListener("DOMContentLoaded", () => {
    
    const formulari = document.getElementById("altaAlumne");
    const divResultat = document.getElementById("missatge");

    formulari.addEventListener("submit", (event) => {
        

        event.preventDefault();

        const nom = document.getElementById("nom").value;
        const edat = document.getElementById("edat").value;
        const email = document.getElementById("email").value;
        // Logica del control de dades
        if ((!nom || !edat || !email)) {
            divResultat.textContent = `Tots els camps són obligatoris`;
            return;
        } else if (edat <= 18){
            divResultat.textContent = `Tens que ser major d'edat, ${nom}}`;
            return;
        // Validació del correu electrònic amb una expressió regular    
        } else if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/.test(email)) {
            divResultat.textContent = `El correu electrònic no és vàlid, ${nom}`;
            return;
        }
        // Alternativa a la validació mes básica
        // else if (!email.includes("@") || !email.includes(".")) {
        //     divResultat.textContent = `El correu electrònic no és vàlid, ${nom}`;
        // }
        else {
            divResultat.textContent = `Benvingut/da, ${nom}!`;
        }
    });
});