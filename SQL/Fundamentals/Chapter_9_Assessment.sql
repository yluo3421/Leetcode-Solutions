/*
    Create a new database called School
    This database should have two tables teachers and students
The students table should have columns for student_id first_name, last_name, 
homeroom_number, phone, email, and graduation year
The teachers table should have columns for teacher_id frist_name, last_name,
homeroom_number, department, email and phoen

    The constraints are mostly up to you
but your table constraints do have to consdier the following
1. We must have a phone number to contact students in case of an emergency
2. We must have ids as the primary key of the tables
3. Phone numbers and emials must be unique to hte individual

    Once you have made the tables , insert a student named Mark Watney
student_id = 1
phone number 777-555-1234
and doesnt have an email
He gradates in 2025 and has 5 as a homeroom number

    Then insert a teacher names Jonas Salk
teacher_id = 1
who has a homeroom numbe rof 5
and is Biology department
His conatct infor is jsalk@school.org
phone number 777-555-4321
*/
CREATE TABLE students(
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    homeroom_number SMALLINT NOT NULL,
    phone VARCHAR(11) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE,
    graduation_year INTEGER NOT NULL,
);

CREATE TABLE teachers(
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    homeroom_number SMALLINT,
    department SMALLINT NOT NULL,
    phone VARCHAR(11) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
);
INSERT INTO students(first_name, last_name, homeroom_number, phone, graduation_year)
VALUES
('Mark', 'Watney', 5, '777-555-1234', 2035);

INSERT INTO teachers(first_name, last_name, department, phone, email)
VALUES
('Jonas', 'Salk', 'Biology', '777-555-4321', 'jsalk@school.org');