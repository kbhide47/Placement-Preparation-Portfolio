-- =========================================================
-- DAY 51 - SQL BASICS
-- =========================================================


-- =========================================================
-- Create Database
-- =========================================================

CREATE DATABASE placement_practice;

USE placement_practice;


-- =========================================================
-- Create Employee Table
-- =========================================================

CREATE TABLE employees (

    employee_id INT PRIMARY KEY,

    name VARCHAR(50),

    department VARCHAR(50),

    salary INT,

    experience INT,

    city VARCHAR(50)

);


-- =========================================================
-- Insert Data
-- =========================================================

INSERT INTO employees
(employee_id, name, department, salary, experience, city)
VALUES

(1, 'Amit', 'IT', 60000, 2, 'Pune'),

(2, 'Riya', 'HR', 45000, 3, 'Mumbai'),

(3, 'Rahul', 'IT', 75000, 5, 'Pune'),

(4, 'Sneha', 'Finance', 55000, 4, 'Delhi'),

(5, 'Karan', 'IT', 50000, 1, 'Mumbai'),

(6, 'Priya', 'HR', 65000, 6, 'Pune'),

(7, 'Arjun', 'Finance', 80000, 7, 'Delhi'),

(8, 'Neha', 'IT', 90000, 8, 'Mumbai'),

(9, 'Vikas', 'Finance', 60000, 3, 'Pune'),

(10, 'Ananya', 'HR', 70000, 5, 'Mumbai');


-- =========================================================
-- Q1. Display all employees.
-- =========================================================

SELECT *
FROM employees;


-- =========================================================
-- Q2. Display only employee name and salary.
-- =========================================================

SELECT
    name,
    salary
FROM employees;


-- =========================================================
-- Q3. Find employees whose salary is greater than 60000.
-- =========================================================

SELECT *
FROM employees
WHERE salary > 60000;


-- =========================================================
-- Q4. Find employees working in IT.
-- =========================================================

SELECT *
FROM employees
WHERE department = 'IT';


-- =========================================================
-- Q5. Find employees from Pune.
-- =========================================================

SELECT *
FROM employees
WHERE city = 'Pune';


-- =========================================================
-- Q6. Find employees with salary between 50000 and 80000.
-- =========================================================

SELECT *
FROM employees
WHERE salary BETWEEN 50000 AND 80000;


-- =========================================================
-- Q7. Find employees whose department is IT or HR.
-- =========================================================

SELECT *
FROM employees
WHERE department IN ('IT', 'HR');


-- =========================================================
-- Q8. Sort employees by salary from highest to lowest.
-- =========================================================

SELECT *
FROM employees
ORDER BY salary DESC;


-- =========================================================
-- Q9. Find the highest salary.
-- =========================================================

SELECT
    MAX(salary) AS highest_salary
FROM employees;


-- =========================================================
-- Q10. Find the average salary.
-- =========================================================

SELECT
    AVG(salary) AS average_salary
FROM employees;


-- =========================================================
-- Q11. Find total salary paid by the company.
-- =========================================================

SELECT
    SUM(salary) AS total_salary
FROM employees;


-- =========================================================
-- Q12. Count the number of employees.
-- =========================================================

SELECT
    COUNT(*) AS employee_count
FROM employees;


-- =========================================================
-- Q13. Find average salary by department.
-- =========================================================

SELECT

    department,

    AVG(salary) AS average_salary

FROM employees

GROUP BY department;


-- =========================================================
-- Q14. Find departments having average salary
-- greater than 60000.
-- =========================================================

SELECT

    department,

    AVG(salary) AS average_salary

FROM employees

GROUP BY department

HAVING AVG(salary) > 60000;


-- =========================================================
-- Q15. Categorize employees based on salary.
-- =========================================================

SELECT

    name,

    salary,

    CASE

        WHEN salary >= 80000
            THEN 'High Salary'

        WHEN salary >= 60000
            THEN 'Medium Salary'

        ELSE
            'Low Salary'

    END AS salary_category

FROM employees;


-- =========================================================
-- END OF DAY 51
-- =========================================================
