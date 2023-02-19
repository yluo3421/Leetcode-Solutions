-- Most Common Aggregate Functions
AVG(); -- return a floating point value
COUNT(); -- return number of rows
MAX(); --
MIN();
SUM();
-- Aggregate functions only in HAVE or WHERE

SELECT MIN(replacement_cost) FROM film;
SELECT MAX(replacement_cost), MIN replacement_cost FROM film;

-- Below is not valid
SELECT MIN(replacement_cost), the_date FROM film;
-- Because aggreagte function only returns one value, 
-- to do the above intention, GROUP BY is needed

SELECT ROUND(AVG(replacement_cost), 2) FROM film;

-- GROUP BY allow us to aggregate columns
/* Categorical column are non-continuous, they can still
be numerical, such as cabin class, Class 1, Class 2, Class 3
*/
SELECT category_col, AGG(data_col)
FROM table_1
WHERE category_col != 'A'
GROUP BY category_col;
-- GROUP BY must occur right after FROM or WHERE

SELECT company, division, SUM(sales)
FROM finance_table
WHERE divison IN ('marketing', 'transport')
GROUP BY compnay, division;
-- company, divison must appear in the GROUP BY
-- But sales does not have to.
-- WHERE statments should not refer to the aggregation result
-- HAVE will help filter those results

SELECT customer_id FROM payment
GROUP BY customer_id
ORDER BY customer_id;
-- this is the same as simple select from

SELECT customer_id, SUM(amount) FROM payment
GROUP BY customer_id
ORDER BY SUM(amount);
-- returns ASC each customer_id's amount

SELECT customer_id, staff_id, SUM(amount) FROM payment
GROUP BY staff_id, customer_id
ORDER BY customer_id;
-- returns how much each customer spent with each staff.

SELECT DATE(payment_date), SUM(amount) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount) DESC;
-- DATE() will take only date info and get rid of seconds
-- this will show highest paid and its date.

-- Challenge
-- We have two staff members, with Staff IDs 1 and 2. We want to give a bonus
-- to the staff member that handled the most payments.
SELECT staff_id, COUNT(amount) FROM payment
GROUP BY staff_id;

/*
Corporate HQ is conducting a study on the relationship between 
replacement cost and a movie MPAA rating (e.g. G, PG, R, etc)
What is the average replacement cost per MPAA rating
*/
SELECT rating, ROUND(AVG(replacement_cost), 2) FROM film
GROUP BY rating;

/*
We are running a promotion to reward
our top 5 customers with coupons.
What are the customer ids of the top 5 customers by total spend?
*/
SELECT customer_id, SUM(amount) FROM payment
GROUP BY SUM(amount) DESC
LIMIT 5;




