info BETWEEN low AND high;
-- is the same as
info > low AND < high;

info < low OR info > high;
-- is the same as
info NOT BETWEEN low AND HIGH;

-- can also be used for dates but needs to be
-- formatted in ISO 8601 YYYY-MM-DD
the_date BETWEEN '2023-01-01' AND '2023-02-01';

-- date time starts at 0:00, this will make 
-- a difference of timestamp

-- Only transactions on Feb 14th will be shown
-- Between is > low and < high
SELECT * FROM payment
WHERE payment_date BETWEEN '2007-02-01' AND '2007-02-15';
