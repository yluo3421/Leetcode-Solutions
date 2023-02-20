'Post' || 'grel'; --concatenation Postgrel

SELECT LENGTH(first_name) FROM customer;

SELECT first_name || last_name
FROM customer;
/*
?column? |
JaredEly
MarySmith
PatriciaJohnson
*/
SELECT UPPER(first_name) || ' ' || last_name AS full_name
FROM customer;
/*
full_name |
JARED Ely
MARY Smith
*/
SELECT LOWER(LEFT(first_name), 1) || '.' || LOWER(last_name) ||'@gmail.com' AS company_email
FROM customer;