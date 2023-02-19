SELECT company, SUM(sales) FROM finance_table
WHERE company != 'Vanguard'
GROUP BY company;
-- we cannot run aggregate function in where because aggregate
-- function runs after GROUP BY.

-- to solve this
SELECT company, SUM(sales) FROM finance_table
WHERE company != 'Vanguard'
GROUP BY company
HAVING SUM(sales) > 1000;

SELECT customer_id, SUM(amount) FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 100;

SELECT store_id, COUNT(*) FROM customer
GROUP BY store_id
HAVING COUNT(*) > 300;

-- challenge
/*
We are launching a platinum service for our most loyal customers.
We will assign platinum status to customers that have had 40
or more transaction payments
What customer_id
*/
SELECT customer_id, COUNT(*) FROM payment
GROUP BY customer_id
HAVING COUNT(*) >= 40;

/*
What are the customer ids of customers who have spent more than $100
in payment transactions with our staff_id member 2
*/
SELECT customer_id, SUM(amount), staff_id FROM payment
WHERE staff_id = 2
GROUP BY customer_id
HAVING SUM(amount) > 100;