import { Base_componentes } from './Base_componentes.js';

export class ProductCard extends Base_componentes {
    //aqui debe de ir algo?
    connectedCallback() {
        this.render(`<h2>Producto</h2>`)
    }

}

