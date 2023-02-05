-- How many payment transactions were greater than $5.00
SELECT COUNT(*) FROM payment
WHERE amount > 5;

-- How many actors have first name that starts with the letter P
SELECT COUNT(*) FROM actor
WHERE first_name LIKE 'P%';

-- How many unique districts are our customers from?
SELECT COUNT(DISTINCT(districts)) FROM customer; 

-- Retrieve the list of names for those distinct districts from the previous question
SELECT DISTINCT(districts) FROM customer;

-- How many films haev a rating of R and a replacement cost between 5 and 15
SELECT COUNT(*) FROM film
WHERE rating = 'R'
AND cost BETWEEN 5 AND 15;

-- How many films have the word Truman somewhere in the title?
SELECT COUNT(*) FROM film
WHERE title LIKE '%Truman%';