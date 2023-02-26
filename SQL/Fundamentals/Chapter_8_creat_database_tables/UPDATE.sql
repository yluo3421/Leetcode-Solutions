UPDATE account
SET last_login = CURRENT_TIMESTAMP
WHERE last_login IS NULL;

UPDATE account
SET last_login = CURRENT_TIMESTAMP;

UPDATE account
SET last_login = created_on;

UPDATE table_1
SET col_1 = table_2.col_2
FROM table_2
WHERE table_1.id = table_2.id;

-- show affected columns
UPDATE account
SET last_login = created_on
RETURNING account_Id, last_login;

