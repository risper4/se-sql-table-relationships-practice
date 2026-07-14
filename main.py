import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

employees_offices = pd.read_sql("""
    SELECT firstName, lastName, city, state
                                FROM employees
                                JOIN offices
                                USING(officeCode)
                                ORDER BY firstName, lastName;
""", conn)
# print(employees_offices)


customers_orders = pd.read_sql("""
    SELECT contactFirstName, contactLastName, orderNumber, orderDate, status
                               FROM customers
                               JOIN orders
                               USING(customerNumber);
""", conn)
print(customers_orders)


customer_payments = pd.read_sql("""
    SELECT contactFirstName, contactLastName, paymentDate, SUM(CAST(amount AS FLOAT)) AS payment_amount
                                FROM customers
                                JOIN payments
                                USING (customerNumber)
                                GROUP BY customerNumber
                                ORDER BY payment_amount DESC;
""", conn)
print(customer_payments)


orders_orderdetails_productdetails = pd.read_sql("""
    SELECT contactFirstName, contactLastName, productName, SUM(CAST(quantityOrdered AS INTEGER)) AS quantity, orderDate
                                                 FROM customers
                                                 JOIN orders
                                                 USING(customerNumber)
                                                 JOIN orderdetails
                                                 USING(orderNumber)
                                                 JOIN products
                                                 USING (productCode)
                                                 GROUP BY customerNumber
                                                 ORDER BY orderDate DESC;
""", conn)
print(orders_orderdetails_productdetails)

conn.close()
