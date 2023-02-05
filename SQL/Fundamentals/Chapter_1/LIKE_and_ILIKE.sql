-- how to return all emails with '@gmail.com'

-- All names that begin with an 'A'
WHERE name_1 LIKE 'A%';
-- All names that end with an 'a'
WHERE name_1 LIKE '%a';
-- Use underscore for single wildcard
WHERE title LIKE 'Mission Impossible _';
-- 'Version#A4', ‘Version#B7'
WHERE the_value LIKE 'Version#__';

-- LIKE is case senstive, while ILIKE is case in-senstive

WHERE name_1 LIKE '_her%';
-- Cheryl
-- Theresa
-- Sherri
