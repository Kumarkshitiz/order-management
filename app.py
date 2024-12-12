from flask import Flask, jsonify, request
from models import create_order, get_order, update_order_item, add_order_item, delete_order_item, delete_order
from config import app, mysql


@app.route('/orders', methods=['POST'])
def create_order_api():
    data = request.get_json()
    order_date = data['order_date']
    customer_id = data['customer_id']
    shipping_contact_mech_id = data['shipping_contact_mech_id']
    billing_contact_mech_id = data['billing_contact_mech_id']
    order_items = data['order_items']

    order_id = create_order(mysql, order_date, customer_id, shipping_contact_mech_id, billing_contact_mech_id, order_items)
    
    return jsonify({"message": "Order created", "order_id": order_id}), 201


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order_api(order_id):
    order, order_items = get_order(mysql, order_id)
    
    if not order:
        return jsonify({"message": "Order is not found!"}), 404

    order_details = {
        "order_id": order[0],
        "order_date": order[1],
        "customer": {"customer_id": order[2], "first_name": order[3], "last_name": order[4]},
        "shipping_address": order[5],
        "billing_address": order[6],
        "order_items": [{"order_item_seq_id": item[0], "product_id": item[1], "product_name": item[2], "quantity": item[3], "status": item[4]} for item in order_items]
    }

    return jsonify(order_details)


@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_item_api(order_id):
    data = request.get_json()
    order_item_seq_id = data['order_item_seq_id']
    quantity = data['quantity']
    status = data['status']
    
    update_order_item(mysql, order_id, order_item_seq_id, quantity, status)

    return jsonify({"message": "Order item updated"}), 200



@app.route('/orders/<int:order_id>/items', methods=['POST'])
def add_order_item_api(order_id):
    data = request.get_json()
    product_id = data['product_id']
    quantity = data['quantity']
    status = data['status']

    add_order_item(mysql, order_id, product_id, quantity, status)

    return jsonify({"message": "item added "}), 201


@app.route('/orders/<int:order_id>/items/<int:order_item_seq_id>', methods=['DELETE'])
def delete_order_item_api(order_id, order_item_seq_id):
    delete_order_item(mysql, order_id, order_item_seq_id)

    return jsonify({"message": "item deleted "}), 200


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order_api(order_id):
    delete_order(mysql, order_id)

    return jsonify({"message": "Order deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
