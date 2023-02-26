DELETE FROM table_1
USING table_2
WHERE table_1.id = table_2.id;

SELECT * FROM job;
INSERT INTO job(job_name)
VALUES
('Cowboy');

DELETE FROM job
WHERE job_name = 'Cowboy'
RETURNING job_id, job_name
-- returns the rows deleted
-- run second time, nothing returns, because nothing deleted


