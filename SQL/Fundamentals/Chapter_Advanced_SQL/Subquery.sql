SELECT AVG(grade)
FROM test_scores;

-- how can we get a list of students who is better than 
-- average grades
SELECT student.grade
FROM test_scores
WHERE grade > (SELECT AVG(grade)
FROM test_scores);

SELECT student.grade
FROM test_scores
WHERE student IN
(SELECT student
FROM honor_roll_table);


-- EXISITS
SELECT column_name
FROM table_1
WHERE EXISTS
(SELECT column_name
FROM table_2
WHERE condition);

SELECT title, rental_rate
FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);

SELECT film_id, title
FROM film
WHERE film_id IN
(SELECT inventory.film_id
FROM rental
INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
WHERE return_date BETWEEN '2005-02-29' AND '2005-05-30')
ORDER BY title;


SELECT first_name, last_name
FROM customer AS c
WHERE EXISTS 
(SELECT * FROM payment AS p
WHERE p.customer_id = c.customer_id
AND p.amount > 11);