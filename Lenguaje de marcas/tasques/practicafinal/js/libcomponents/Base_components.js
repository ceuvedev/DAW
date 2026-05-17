// libcomponents/base_component.js
export class BaseComponent extends HTMLElement {
    constructor() {
    super();
    this.attachShadow({ mode: "open" });
    }
    
    render(html) {
    this.shadowRoot.innerHTML = html;
    }}