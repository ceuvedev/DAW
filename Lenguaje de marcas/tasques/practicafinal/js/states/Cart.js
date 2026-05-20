// state/Cart.js
export const Cart = {
    items: [],
    listeners: [],
    subscribe(callback) {
        this.listeners.push(callback);
    },
    notify() {
        this.listeners.forEach(cb => cb(this.items));
    },
    add(product) {
        this.items.push(product);
        this.notify();
    },
    remove(productId) {
        this.items = this.items.filter(item => item.id !== productId);
        this.notify();
    },
    clear() {
        this.items = [];
        this.notify();
    }
};
