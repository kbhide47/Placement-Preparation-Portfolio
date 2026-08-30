-- =========================================================
-- DAY 54 - SQL WINDOW FUNCTIONS
-- =========================================================


-- =========================================================
-- Create Database
-- =========================================================

CREATE DATABASE day54_window;

USE day54_window;


-- =========================================================
-- Create Employees Table
-- =========================================================

CREATE TABLE employees (

    employee_id INT PRIMARY KEY,

    employee_name VARCHAR(50),

    department VARCHAR(50),

    salary INT,

    experience INT

);


-- =========================================================
-- Insert Data
-- =========================================================

INSERT INTO employees
(employee_id, employee_name, department, salary, experience)
VALUES

(1, 'Amit', 'IT', 60000, 2),

(2, 'Riya', 'HR', 55000, 3),

(3, 'Rahul', 'IT', 85000, 5),

(4, 'Sneha', 'Finance', 50000, 2),

(5, 'Karan', 'IT', 100000, 8),

(6, 'Priya', 'HR', 90000, 6),

(7, 'Arjun', 'Finance', 95000, 7),

(8, 'Neha', 'IT', 70000, 4),

(9, 'Vikas', 'Finance', 65000, 3),

(10, 'Ananya', 'HR', 75000, 5);


-- =========================================================
-- Q1. What is a Window Function?
-- =========================================================

-- A window function performs a calculation
-- across a set of related rows without
-- combining those rows into one row.
--
-- Unlike GROUP BY:
--
-- GROUP BY reduces rows.
--
-- Window functions keep the original rows.


-- =========================================================
-- Q2. ROW_NUMBER()
-- Give every employee a unique row number
-- based on salary.
-- =========================================================

SELECT

    employee_name,

    salary,

    ROW_NUMBER() OVER (
        ORDER BY salary DESC
    ) AS row_num

FROM employees;


-- =========================================================
-- Q3. RANK()
-- Rank employees based on salary.
-- =========================================================

SELECT

    employee_name,

    salary,

    RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank

FROM employees;


-- =========================================================
-- Q4. DENSE_RANK()
-- Rank employees using DENSE_RANK().
-- =========================================================

SELECT

    employee_name,

    salary,

    DENSE_RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank

FROM employees;


-- =========================================================
-- Q5. RANK() vs DENSE_RANK()
-- =========================================================

-- Suppose salaries are:
--
-- 100000
-- 90000
-- 90000
-- 70000
--
-- RANK():
--
-- 1
-- 2
-- 2
-- 4
--
-- DENSE_RANK():
--
-- 1
-- 2
-- 2
-- 3
--
-- RANK skips numbers after ties.
-- DENSE_RANK does not skip numbers.


-- =========================================================
-- Q6. PARTITION BY
-- Rank employees within each department.
-- =========================================================

SELECT

    employee_name,

    department,

    salary,

    RANK() OVER (

        PARTITION BY department

        ORDER BY salary DESC

    ) AS department_rank

FROM employees;


-- =========================================================
-- Q7. Find the highest-paid employee
-- in each department.
-- =========================================================

SELECT *

FROM

(
    SELECT

        employee_name,

        department,

        salary,

        ROW_NUMBER() OVER (

            PARTITION BY department

            ORDER BY salary DESC

        ) AS rn

    FROM employees

) AS ranked_employees

WHERE rn = 1;


-- =========================================================
-- Q8. Find the top 2 highest-paid employees
-- from each department.
-- =========================================================

SELECT *

FROM

(
    SELECT

        employee_name,

        department,

        salary,

        ROW_NUMBER() OVER (

            PARTITION BY department

            ORDER BY salary DESC

        ) AS rn

    FROM employees

) AS ranked_employees

WHERE rn <= 2;


-- =========================================================
-- Q9. Find employees earning more than
-- their department average.
-- =========================================================

SELECT

    employee_name,

    department,

    salary,

    AVG(salary) OVER (

        PARTITION BY department

    ) AS department_average

FROM employees;


-- =========================================================
-- Q10. Find salary difference from
-- department average.
-- =========================================================

SELECT

    employee_name,

    department,

    salary,

    AVG(salary) OVER (

        PARTITION BY department

    ) AS department_average,

    salary -

    AVG(salary) OVER (

        PARTITION BY department

    ) AS difference

FROM employees;


-- =========================================================
-- Q11. LAG()
-- Compare employee salary with previous salary
-- when ordered by salary.
-- =========================================================

SELECT

    employee_name,

    salary,

    LAG(salary) OVER (

        ORDER BY salary

    ) AS previous_salary

FROM employees;


-- =========================================================
-- Q12. LEAD()
-- Compare employee salary with next salary.
-- =========================================================

SELECT

    employee_name,

    salary,

    LEAD(salary) OVER (

        ORDER BY salary

    ) AS next_salary

FROM employees;


-- =========================================================
-- Q13. Calculate running total of salaries.
-- =========================================================

SELECT

    employee_name,

    salary,

    SUM(salary) OVER (

        ORDER BY employee_id

    ) AS running_total

FROM employees;


-- =========================================================
-- Q14. Calculate cumulative salary
-- separately for each department.
-- =========================================================

SELECT

    employee_name,

    department,

    salary,

    SUM(salary) OVER (

        PARTITION BY department

        ORDER BY employee_id

    ) AS department_running_total

FROM employees;


-- =========================================================
-- Q15. Find the highest-paid employee
-- in each department using DENSE_RANK().
-- =========================================================

WITH ranked_employees AS

(

    SELECT

        employee_name,

        department,

        salary,

        DENSE_RANK() OVER (

            PARTITION BY department

            ORDER BY salary DESC

        ) AS salary_rank

    FROM employees

)

SELECT *

FROM ranked_employees

WHERE salary_rank = 1;


-- =========================================================
-- END OF DAY 54
-- =========================================================
