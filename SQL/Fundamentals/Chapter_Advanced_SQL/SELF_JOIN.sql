-- The self join can be viewed as a join of two copies of the same table
-- The table is not acutally copied
-- It is necessary to use alias for the table
SELECT table_1.col_1, table_2.col_1
FROM original_table AS table_1
JOIN original_table AS table_2 ON
table_1.some_col = table_2.other_col;

/*
Employees
emp_id  | name  | report_id
1        Andrew   3
2        Bob      3
3        Charlie  4
4        Dvaid    1
*/
-- We want to show the employee name and their report recipient name
SELECT emp.name, report.name AS rep
FROM employees AS emp
JOIN employees AS report ON
emp.emp_id = report.report_id
/*
name | rep
And     Char
Bob     Char
*/

SELECT f1.title, f2.length, f1.length
FROM film AS f1
INNER JOIN film AS f2 ON
f1.film_id != f2.film_id
AND f1.length = f2.length;

