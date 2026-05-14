class TarjetaProducte extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
    }

    connectedCallback() {
        this.render();
    }

    render() {
        const nombre = this.querySelector('nom')?.textContent || "Nombre";
        const precio = this.querySelector('precio')?.textContent || "Precio";
        const descripcion = this.querySelector('descripcion')?.textContent || "Descripcion";

        this.shadowRoot.innerHTML = `
            <style>
                .tarjeta {
                    border: 5px solid #9fd9f6;
                    border-radius: 10px;
                    padding: 15px;
                    margin: 10px;
                    width: 250px;
                    background: #4a4a4a;
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                    text-align: center;
                }
                .tarjeta:hover {
                    border: 5px solid #f9fc5c;
                    border-radius: 10px;
                    padding: 15px;
                    margin: 10px;
                    width: 250px;
                    background: #4a4a4a;
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                    text-align: center;
                
                }
                .tarjeta h2, .tarjeta p {
                    color: #7de2fc;
                    margin: 5px 0;
                }
            </style>
            <div class="tarjeta">
                <h2>${nombre}</h2>
                <p>${precio}</p>
                <p>${descripcion}</p>
            </div>
        `;
    }
}

customElements.define('tarjeta-producte', TarjetaProducte);