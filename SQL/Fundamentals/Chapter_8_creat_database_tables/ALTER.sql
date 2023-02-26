/*
Adding, dropping, or renaming columns
changing a column's data type
set default values for a column
add check constraints
rename table
*/

ALTER table_1 action
ADD COLUMN col_1;
ALTER table_1 action
DROP COLUMN col_1;
ALTER table_1 action
ALTER COLUMN col_1
DROP DEFAULT;

CREATE TABLE information(
    info_id SERIAL PRIMARY KEY,
    title VARCHAR(500) NOT NULL.
    person VARCHAR(50) NOT NULL UNIQUE
);

-- rename
ALTER TABLE information
RENAME TO new_info;

ALTER TABLE new_info
RENAME COLUMN person TO people

ALTER TABLE new_info
ALTER COLUMN people DROP NOT NULL;

