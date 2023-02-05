SELECT col_1, col_2
FROM table_1
WHERE conditions;

SELECT name_1, choice FROM table_1
WHERE name_1 = 'David' AND choice = 'RED';

-- Find patients that is not affected by patient 2
-- the OR part will handle those who are not affected
-- otherwise it will only return those with infected_by_id and not equal to 2
SELECT name_1 FROM patients WHERE infected_by_id <> 2 OR infected_by_id IS NULL;

SELECT COUNT(title) FROM film
WHERE rental_rate > 4 AND replacement_cost >= 19.99
AND rating != 'R' or rating = 'PG-13';

-- A customer forgot their wallet at our store
-- What is the email for the custormer with the name Nancy Thomas
SELECT email FROM customer
WHERE first_name = 'Nancy' AND last_name = 'Thomas';

-- Could you give them the description for the movie "Outlaw Hanky"
SELECT description_ FROM film
WHERE title = 'Outlaw Hanky'

-- customer late on movie return, get phone number of the customer
-- from address '259 Ipoh Drive'
SELECT phone FROM address_table
WHERE address_col = '259 Ipoh Drive';