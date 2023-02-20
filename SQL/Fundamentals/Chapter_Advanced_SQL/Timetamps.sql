SELECT NOW();
-- return the current timestamps

SELECT TIMEOFDAY();
-- return string day, date, time, year, timezone

SELECT CURRENT_TIME;
-- return current time with timezone

SELECT CURRENT_DATE;
-- return date string

EXTRACT();
-- allow to extract or obatina a sub-component of a date value
EXTRACT(YEAR FROM date_col);

AGE();
-- calculates and returns the current age given a timestamp
AGE(date_col);
-- returns 13 years 1 mon 5 days 01:34:13.003423

TO_CHAR();
-- general funciton to convert data types to text
TO_CHAR(date_col, 'mm-dd-yyyy');

SELECT EXTRACT(YEAR FROM payment_date) 
AS pay_month
FROM payment;

SELECT AGE(payment_date)
FROM payment;

SELECT TO_CHAR(payment_date, '');
-- refer to the documentation for speicif type of output
-- MONTH, MM, Month, mon, YYYY, YY, 

SELECT DISTINCT(TO_CHAR(payment_date, 'MONTH'))
FROM payment;
-- return the unqiue month in format of capital full spelled month

-- How many payments occurred on a monday
SELECT COUNT(*)
FROM payment
WHERE EXTRACT(dow FROM payment_date) = 1;
-- SQL consdier sunday start of week as index 0

