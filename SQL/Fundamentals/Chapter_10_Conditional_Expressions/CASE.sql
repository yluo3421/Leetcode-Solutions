/*
CASE is like if/else
General CASE and a CASE expression
*/
CASE
    WHEN condition_1 THEN result_1
    WHEN condition_2 THEN result_2
    ELSE result_3
END;

/*
|a  |
|1  |
|2  |
*/
SELECT a,
CASE 
WHEN a = 1 THEN 'one'
WHEN a = 2 THEN 'two'
ELSE 'other' AS label
END
FROM test;
/*
a   | label
1   | one
2   | two
*/


SELECT col_1,
CASE col_1
    WHEN value_1 THEN result_1
    ELSE 'other'
END
FROM test;

SELECT customer_id,
CASE
    WHEN (customer_id <= 100) THEN 'Premium'
    WHEN (customer_id BETWEEN 100 AND 200) THEN 'Plus'
    ELSE 'Normal'
END AS customer_class
FROM customer;

-- can I have different type of data in return?

SELECT customer_id,
CASE customer_id
    WHEN 2 THEN 'Winner'
    WHEN 5 THEN 'Second Place'
    ELSE 'Normal'
END AS raffle_results
FROM customer;

-- return number of 0.99 rentals
SELECT
SUM(CASE rental_rate
    WHEN 0.99 THEN 1
    ELSE 0
END) AS number_of_bargains
FROM film;

-- 1 & 0 here stands for boolean?
SELECT
SUM(CASE rental_rate
    WHEN 0.99 THEN 1
    ELSE 0
END) AS bargains,
SUM(CASE rental_rate
    WHEN 2.99 THEN 1
    ELSE 0
END) AS regular
SUM(CASE rental_rate
    WHEN 4.99 THEN 1
    ELSE 0
END) AS premium
FROM film;

-- CHALLENGE
-- compare various amounts of films we have per movie rating
-- r pg pg 13
-- boring