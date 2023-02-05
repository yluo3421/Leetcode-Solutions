-- return 5 most recent payment that is not 0 amount
SELECT * FROM payment
WHERE amount != 0.00
ORDER BY payment_date DESC
LIMIT 5;

-- We want to reward our first 10 paying customers
-- What are the customers ids of the first 10 customers who created a payment?
SELECT customer_id FROM payment
WHERE amount != 0.00
ORDER BY payment_date ASC
LIMIT 10;

/* A customer wants to quickly rent a video to watch
over their short lunch break.
What are the titles of the 5 shortest in runtime movies?
*/
SELECT title FROM movie
ORDER BY runtime ASC
LIMIT 5;

/* If the customer can watch any movie that is 50 min or less in runtime
How many optinos does she have */
SELECT COUNT(title) FROM movie
WHERE runtime <= 50;