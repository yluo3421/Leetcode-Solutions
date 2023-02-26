/*
A view is a database object that is of a stored query/
A view cna be accesssed as a virtual storage.
*/
CREATE VIEW customer_info AS 
SELECT first_name, last_name, address FROM customer
INNER JOIN address 
ON customer.address_id = address.address_id;

SELECT * FROM customer_info;
-- will return the same thing.