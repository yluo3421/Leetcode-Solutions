-- AS
-- INNER JOINS
-- OUTER JOINS
-- FULL JOINS
-- UNIONS

SELECT col_1 AS new_name FROM table_1;

SELECT amount AS rental_price FROM payment;
-- This will return the column name AS rental_price

SELECT SUM(amount) AS net_revenue FROM payment;

-- AS operator gets executed at the very end of a query.
-- Meaning we cannot use ALIAS inside a WHERE operator.

SELECT customer_id, SUM(amount) AS total_spent
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100;
-- YOU cannot use HAVING total_spent > 100;
-- error: column "total_spent" does not exist

