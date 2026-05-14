class TextoEncapsulado extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
    }

    connectedCallback() {
        this.render();
    }

    render() {
        const encabezado = this.querySelector('encabezado')?.textContent || "Encabezado";
        const texto = this.querySelector('texto')?.textContent || "texto";
        this.shadowRoot.innerHTML = `
            <style>

                h2, p {
                    color: #125a6e;
                    margin: 5px 0;
                }
            </style>
            <div class="tarjeta">
                <h2>${encabezado}</h2>
                <p>${texto}</p>

            </div>
        `;
    }
}

customElements.define('texto-encapsulado', TextoEncapsulado);