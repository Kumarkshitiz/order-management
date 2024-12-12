# Order Management API

This project provides a RESTful API for managing customers, orders, and products.

## Features
- **Create Orders**: Add a new order with customer and product details.
- **Retrieve Order Details**: Get full information about a specific order.
- **Update Orders**: Modify shipping or billing details of an order.
- **Delete Orders**: Remove an order and its associated items.
- **Manage Order Items**: Add, update, or delete items within an order.

## API Endpoints
- `POST /orders` - Create a new order.
- `GET /orders/<order_id>` - Retrieve details of a specific order.
- `DELETE /orders/<order_id>` - Delete an order.
- `POST /orders/<order_id>/items` - Add an item to an order.
- `PUT /orders/<order_id>/items/<order_item_seq_id>` - Update an order item.
- `DELETE /orders/<order_id>/items/<order_item_seq_id>` - Delete an order item.

## Getting Started
1. Clone the repository: `git clone <repository_url>`
2. Set up your database with the provided schema.
3. Run the application: `flask run`
5. Open your browser at `http://localhost:5000` to see the API documentation.

## Testing
Use Postman to test the endpoints. Example requests can be found in the documentation.
