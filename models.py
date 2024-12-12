def create_order(mysql, order_date, customer_id, shipping_contact_mech_id, billing_contact_mech_id, order_items):
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO Order_Header (order_date, customer_id, shipping_contact_mech_id, billing_contact_mech_id)
                      VALUES (%s, %s, %s, %s)''', (order_date, customer_id, shipping_contact_mech_id, billing_contact_mech_id))
    mysql.connection.commit()
    order_id = cursor.lastrowid

    for item in order_items:
        cursor.execute('''INSERT INTO Order_Item (order_id, product_id, quantity, status)
                          VALUES (%s, %s, %s, %s)''', (order_id, item['product_id'], item['quantity'], item['status']))
    mysql.connection.commit()
    cursor.close()
    
    return order_id


def get_order(mysql, order_id):
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT o.order_id, o.order_date, o.customer_id, c.first_name, c.last_name, o.shipping_contact_mech_id, o.billing_contact_mech_id
                      FROM Order_Header o
                      JOIN Customer c ON o.customer_id = c.customer_id
                      WHERE o.order_id = %s''', (order_id,))
    order = cursor.fetchone()

    cursor.execute('''SELECT oi.order_item_seq_id, oi.product_id, p.product_name, oi.quantity, oi.status
                      FROM Order_Item oi
                      JOIN Product p ON oi.product_id = p.product_id
                      WHERE oi.order_id = %s''', (order_id,))
    order_items = cursor.fetchall()
    cursor.close()

    return order, order_items


def update_order_item(mysql, order_id, order_item_seq_id, quantity, status):
    cursor = mysql.connection.cursor()
    cursor.execute('''UPDATE Order_Item
                      SET quantity = %s, status = %s
                      WHERE order_id = %s AND order_item_seq_id = %s''',
                   (quantity, status, order_id, order_item_seq_id))
    mysql.connection.commit()
    cursor.close()


def add_order_item(mysql, order_id, product_id, quantity, status):
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO Order_Item (order_id, product_id, quantity, status)
                      VALUES (%s, %s, %s, %s)''', (order_id, product_id, quantity, status))
    mysql.connection.commit()
    cursor.close()


def delete_order_item(mysql, order_id, order_item_seq_id):
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE FROM Order_Item WHERE order_id = %s AND order_item_seq_id = %s''',
                   (order_id, order_item_seq_id))
    mysql.connection.commit()
    cursor.close()


def delete_order(mysql, order_id):
    cursor = mysql.connection.cursor()
    cursor.execute('''DELETE FROM Order_Item WHERE order_id = %s''', (order_id,))
    cursor.execute('''DELETE FROM Order_Header WHERE order_id = %s''', (order_id,))
    mysql.connection.commit()
    cursor.close()
