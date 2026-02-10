
document.addEventListener("DOMContentLoaded", () => {
    
    const formulari = document.getElementById("altaAlumne");
    const divResultat = document.getElementById("benvinguda");

    formulari.addEventListener("submit", (event) => {
        

        event.preventDefault();

        const nom = document.getElementById("nom").value;
        const email = document.getElementById("email").value;

        divResultat.textContent = `Benvingut/da ${nom} (${email})`;
        

    });
});