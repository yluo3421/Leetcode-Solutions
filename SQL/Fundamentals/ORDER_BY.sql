-- return 5 most recent payment
SELECT * FROM payment
ORDER BY payment_date DESC
LIMIT 5;