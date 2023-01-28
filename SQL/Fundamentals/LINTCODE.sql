
-- SELECT connected tables
SELECT
t1.student_name
,t1.phone
,t2.hometown
,t2.address
FROM students t1 LEFT JOIN enrollments t2
ON t1.id = t2.student_id;

-- Write a SQL query to find all students with the same name in the students table.
SELECT name FROM students GROUP BY name HAVING COUNT(name)>1;