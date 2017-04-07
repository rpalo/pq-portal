// Turns the plastic homepage into a quick flashy search/sortable page

const plastics = [
    {
        id: 1,
        number: "This one",
        description: "A good boy",
        quantity: 55,
        purchase_date: "1/1/25",
        vendor: "Vendor 1",
        purchase_price: 1.22,
        order_threshhold: 20
    },
    {
        id: 2,
        number: "That one",
        description: "A good boy",
        quantity: 55,
        purchase_date: "1/1/25",
        vendor: "Vendor 1",
        purchase_price: 1.22,
        order_threshhold: 20
    },
    {
        id: 3,
        number: "This other one",
        description: "A good boy",
        quantity: 55,
        purchase_date: "1/1/25",
        vendor: "Vendor 1",
        purchase_price: 1.22,
        order_threshhold: 20
    }


class Plastic {
    constructor(plastic_data) {
        this.id = plastic_data.id;
        this.number = plastic_data.number;
        this.description = plastic_data.description;
        this.quantity = plastic_data.quantity;
        this.purchase_date = plastic_data.purchase_date;
        this.vendor = plastic_data.vendor;
        this.purchase_price = plastic_data.purchase_price;
        this.order_threshhold = plastic_data.order_threshhold;
    }
}