class TarjetaProducte extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
    }

    connectedCallback() {
        this.render();
        this.agregarEventoBoton();
    }

    render() {
        
        const nombre = this.getAttribute('nom') || "Nombre";
        const precio = this.getAttribute('precio') || "Precio";
        const descripcion = this.getAttribute('descripcion') || "Descripcion";


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
                .h2,. p {
                    color: #7de2fc;
                    margin: 5px 0;
                }

                button {
                    background: #f9fc5c;
                    color: #333;
                    border: none;
                    border-radius: 5px;
                    padding: 10px 15px;
                    margin-top: 15px;
                    cursor: pointer;
                    font-weight: bold;
                    font-size: 1rem;
                    transition: background 0.3s ease;
                    width: 100%;
                }
                button:hover {
                    background: #e5e83e;
                }
            </style>
            <div class="tarjeta">
                <h2>${nombre}</h2>
                <p>${precio}</p>
                <p>${descripcion}</p>
                <img src="img/${nombre}.jpg" alt="${nombre}" style="width:100%; height:auto; border-radius: 5px; margin-top: 10px;">
                <button class="btn-carrito">🛒 Añadir al carrito</button>
            </div>
        `;
    }
    agregarEventoBoton() {
        // Esperamos un momento a que el DOM esté listo
        setTimeout(() => {
            const boton = this.shadowRoot.querySelector('.btn-carrito');
            const nombre = this.getAttribute('nom') || "Producto";
            const precio = this.getAttribute('precio') || "0";
            
            if (boton) {
                boton.addEventListener('click', () => {
                    alert(`${nombre} (${precio}) añadido al carrito`);
                });
            }
        }, 0);
    }
}

customElements.define('tarjeta-producte', TarjetaProducte);