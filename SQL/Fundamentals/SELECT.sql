-- SELECT column_name FROM table_name

-- SELECT multiple columns with the sequence
SELECT c1, c3, c2 FROM table_1

-- SELECT all columns
SELECT * FROM table_2

-- SELECT DISTINCT

-- SELECT connected tables
SELECT
t1.student_name
,t1.phone
,t2.hometown
,t2.address
FROM students t1 LEFT JOIN enrollments t2
ON t1.id = t2.student_id;