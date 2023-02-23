INSERT INTO table_1(column_name, column_name,...)
SELECT column_name
FROM another_table
WHERE condition;

-- SERIAL columns do not need to be provided a value
-- what would happen if I provided one?

INSERT INTO account(username, password, email, created_on)
VALUES
('Jose', 'password','jose@mail.com',CURRENT_TIMESTAMP);

INSERT INTO job(job_name)
VALUES
('Application Engineer');

INSERT INTO job(job_name)
VALUES
('President');

INSERT INTO account_job(user_id, job_id, hire_date)
VALUES
(1,1,CURRENT_TIMESTAMP);