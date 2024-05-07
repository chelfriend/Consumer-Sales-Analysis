-- SQL script for data extraction from customer sales databases

-- Connect to the database
USE YourDatabaseName;

-- Extract data from multiple related tables
SELECT 
    customers.customer_id,
    customers.customer_name,
    orders.order_id,
    orders.order_date,
    order_details.product_id,
    products.product_name,
    order_details.quantity,
    order_details.unit_price
FROM 
    customers
JOIN 
    orders ON customers.customer_id = orders.customer_id
JOIN 
    order_details ON orders.order_id = order_details.order_id
JOIN 
    products ON order_details.product_id = products.product_id
WHERE 
    orders.order_date BETWEEN '2023-01-01' AND '2023-12-31';
