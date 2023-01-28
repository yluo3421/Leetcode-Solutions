SELECT * FROM actor;
-- actor_id, first_name, last_name, last_update

SELECT first_name FROM actor;

-- CHALLENGE
-- Use a SELECT statement to grab the first and last names of every customer and their email address
SELECT first_name, last_name, email FROM customer;

-- SELECT DISTINCT
SELECT DISTINCT release_year FROM film;

-- SELECT COUNT
SELECT COUNT(name_1) FROM table_1;
-- returan number of rows in the table
-- below return the same things
SELECT COUNT(*) FROM table_1;
SELECT COUNT(col_1) FROM table_1;

-- How many unique names in the table?
SELECT COUNT(DISTINCT name_1) FROM table_1
-- this returns 3, it wont tell what are the distinct names



