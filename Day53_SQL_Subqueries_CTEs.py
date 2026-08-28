-- =========================================================
-- DAY 53 - SQL SUBQUERIES + CTEs
-- =========================================================


-- =========================================================
-- Create Database
-- =========================================================

CREATE DATABASE day53_sql;

USE day53_sql;


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
-- Q1. What is a Subquery?
-- =========================================================

-- A subquery is a query written inside another query.
--
-- Example:
--
-- SELECT *
-- FROM employees
-- WHERE salary >
--      (SELECT AVG(salary) FROM employees);
--
-- Inner query executes first.
-- Its result is used by the outer query.


-- =========================================================
-- Q2. Find employees earning more than
-- the overall average salary.
-- =========================================================

SELECT *

FROM employees

WHERE salary >

    (
        SELECT AVG(salary)
        FROM employees
    );


-- =========================================================
-- Q3. Find the employee with the highest salary.
-- =========================================================

SELECT *

FROM employees

WHERE salary =

    (
        SELECT MAX(salary)
        FROM employees
    );


-- =========================================================
-- Q4. Find employees earning more than
-- the minimum salary.
-- =========================================================

SELECT *

FROM employees

WHERE salary >

    (
        SELECT MIN(salary)
        FROM employees
    );


-- =========================================================
-- Q5. Find employees working in departments
-- where at least one employee earns more than 90000.
-- =========================================================

SELECT *

FROM employees

WHERE department IN

    (
        SELECT department

        FROM employees

        WHERE salary > 90000
    );


-- =========================================================
-- Q6. Find employees whose salary is greater
-- than the average salary of the IT department.
-- =========================================================

SELECT *

FROM employees

WHERE salary >

    (
        SELECT AVG(salary)

        FROM employees

        WHERE department = 'IT'
    );


-- =========================================================
-- Q7. Find the second-highest salary.
-- =========================================================

SELECT MAX(salary) AS second_highest_salary

FROM employees

WHERE salary <

    (
        SELECT MAX(salary)
        FROM employees
    );


-- =========================================================
-- Q8. Find employees who earn the
-- second-highest salary.
-- =========================================================

SELECT *

FROM employees

WHERE salary =

    (
        SELECT MAX(salary)

        FROM employees

        WHERE salary <

            (
                SELECT MAX(salary)
                FROM employees
            )
    );


-- =========================================================
-- Q9. What is EXISTS?
-- =========================================================

-- EXISTS checks whether a subquery
-- returns at least one row.
--
-- It returns TRUE if matching data exists.
--
-- Example:
--
-- SELECT *
-- FROM employees e
-- WHERE EXISTS (
--
--     SELECT 1
--     FROM employees x
--     WHERE x.department = e.department
--     AND x.salary > 90000
--
-- );


-- =========================================================
-- Q10. Find departments that have
-- at least one employee earning more than 90000.
-- =========================================================

SELECT DISTINCT e.department

FROM employees e

WHERE EXISTS

    (
        SELECT 1

        FROM employees x

        WHERE x.department = e.department

        AND x.salary > 90000
    );


-- =========================================================
-- Q11. What is a CTE?
-- =========================================================

-- CTE = Common Table Expression.
--
-- A CTE creates a temporary named result
-- that can be used by the main query.
--
-- Syntax:
--
-- WITH cte_name AS
-- (
--     SELECT ...
-- )
-- SELECT *
-- FROM cte_name;


-- =========================================================
-- Q12. Create a CTE containing
-- employees earning more than 70000.
-- =========================================================

WITH high_salary_employees AS

(
    SELECT *

    FROM employees

    WHERE salary > 70000
)

SELECT *

FROM high_salary_employees;


-- =========================================================
-- Q13. Calculate average salary using a CTE.
-- =========================================================

WITH salary_data AS

(
    SELECT
        AVG(salary) AS average_salary

    FROM employees
)

SELECT *

FROM salary_data;


-- =========================================================
-- Q14. Find departments whose average salary
-- is greater than 70000 using a CTE.
-- =========================================================

WITH department_salary AS

(
    SELECT

        department,

        AVG(salary) AS average_salary

    FROM employees

    GROUP BY department
)

SELECT *

FROM department_salary

WHERE average_salary > 70000;


-- =========================================================
-- Q15. Use multiple CTEs to analyze salaries.
-- =========================================================

WITH department_stats AS

(
    SELECT

        department,

        COUNT(*) AS employee_count,

        AVG(salary) AS average_salary,

        MAX(salary) AS maximum_salary,

        MIN(salary) AS minimum_salary

    FROM employees

    GROUP BY department
),

high_paying_departments AS

(
    SELECT *

    FROM department_stats

    WHERE average_salary > 70000
)

SELECT *

FROM high_paying_departments;


-- =========================================================
-- END OF DAY 53
-- =========================================================
