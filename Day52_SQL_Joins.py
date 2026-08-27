-- =========================================================
-- DAY 52 - SQL JOINS
-- =========================================================


-- =========================================================
-- Create Database
-- =========================================================

CREATE DATABASE day52_joins;

USE day52_joins;


-- =========================================================
-- Create Employees Table
-- =========================================================

CREATE TABLE employees (

    employee_id INT PRIMARY KEY,

    employee_name VARCHAR(50),

    department_id INT,

    salary INT,

    manager_id INT

);


-- =========================================================
-- Insert Employees
-- =========================================================

INSERT INTO employees
(employee_id, employee_name, department_id, salary, manager_id)
VALUES

(1, 'Amit', 10, 60000, 5),

(2, 'Riya', 20, 55000, 6),

(3, 'Rahul', 10, 75000, 5),

(4, 'Sneha', 30, 50000, 7),

(5, 'Karan', 10, 100000, NULL),

(6, 'Priya', 20, 90000, NULL),

(7, 'Arjun', 30, 95000, NULL),

(8, 'Neha', NULL, 45000, 5);


-- =========================================================
-- Create Departments Table
-- =========================================================

CREATE TABLE departments (

    department_id INT PRIMARY KEY,

    department_name VARCHAR(50),

    location VARCHAR(50)

);


-- =========================================================
-- Insert Departments
-- =========================================================

INSERT INTO departments
(department_id, department_name, location)
VALUES

(10, 'IT', 'Pune'),

(20, 'HR', 'Mumbai'),

(30, 'Finance', 'Delhi'),

(40, 'Marketing', 'Bangalore');


-- =========================================================
-- Q1. What is a JOIN?
-- =========================================================

-- A JOIN combines rows from two or more tables
-- using a related column.
--
-- Example:
--
-- employees.department_id
--          ↓
-- departments.department_id


-- =========================================================
-- Q2. INNER JOIN
-- Find employees along with department names.
-- =========================================================

SELECT

    e.employee_name,

    d.department_name

FROM employees e

INNER JOIN departments d

    ON e.department_id = d.department_id;


-- =========================================================
-- Q3. LEFT JOIN
-- Display ALL employees and their departments.
-- =========================================================

SELECT

    e.employee_name,

    d.department_name

FROM employees e

LEFT JOIN departments d

    ON e.department_id = d.department_id;


-- =========================================================
-- Q4. RIGHT JOIN
-- Display ALL departments and matching employees.
-- =========================================================

SELECT

    e.employee_name,

    d.department_name

FROM employees e

RIGHT JOIN departments d

    ON e.department_id = d.department_id;


-- =========================================================
-- Q5. Find employees who do NOT have a department.
-- =========================================================

SELECT

    e.employee_name,

    e.department_id

FROM employees e

LEFT JOIN departments d

    ON e.department_id = d.department_id

WHERE d.department_id IS NULL;


-- =========================================================
-- Q6. Find departments with NO employees.
-- =========================================================

SELECT

    d.department_name

FROM departments d

LEFT JOIN employees e

    ON d.department_id = e.department_id

WHERE e.employee_id IS NULL;


-- =========================================================
-- Q7. Find employees working in IT.
-- =========================================================

SELECT

    e.employee_name,

    d.department_name

FROM employees e

INNER JOIN departments d

    ON e.department_id = d.department_id

WHERE d.department_name = 'IT';


-- =========================================================
-- Q8. Find employees earning more than 70000
-- along with their department.
-- =========================================================

SELECT

    e.employee_name,

    e.salary,

    d.department_name

FROM employees e

INNER JOIN departments d

    ON e.department_id = d.department_id

WHERE e.salary > 70000;


-- =========================================================
-- Q9. Count employees in each department.
-- =========================================================

SELECT

    d.department_name,

    COUNT(e.employee_id) AS employee_count

FROM departments d

LEFT JOIN employees e

    ON d.department_id = e.department_id

GROUP BY d.department_name;


-- =========================================================
-- Q10. Find average salary in each department.
-- =========================================================

SELECT

    d.department_name,

    AVG(e.salary) AS average_salary

FROM departments d

INNER JOIN employees e

    ON d.department_id = e.department_id

GROUP BY d.department_name;


-- =========================================================
-- Q11. Find departments whose average salary
-- is greater than 70000.
-- =========================================================

SELECT

    d.department_name,

    AVG(e.salary) AS average_salary

FROM departments d

INNER JOIN employees e

    ON d.department_id = e.department_id

GROUP BY d.department_name

HAVING AVG(e.salary) > 70000;


-- =========================================================
-- Q12. SELF JOIN
-- Display employee and manager names.
-- =========================================================

SELECT

    e.employee_name AS employee,

    m.employee_name AS manager

FROM employees e

LEFT JOIN employees m

    ON e.manager_id = m.employee_id;


-- =========================================================
-- Q13. Find employees earning more than their manager.
-- =========================================================

SELECT

    e.employee_name AS employee,

    e.salary AS employee_salary,

    m.employee_name AS manager,

    m.salary AS manager_salary

FROM employees e

INNER JOIN employees m

    ON e.manager_id = m.employee_id

WHERE e.salary > m.salary;


-- =========================================================
-- Q14. CROSS JOIN
-- Generate every employee-department combination.
-- =========================================================

SELECT

    e.employee_name,

    d.department_name

FROM employees e

CROSS JOIN departments d;


-- =========================================================
-- Q15. Join + GROUP BY + HAVING
--
-- Find departments having at least 2 employees
-- and average salary greater than 60000.
-- =========================================================

SELECT

    d.department_name,

    COUNT(e.employee_id) AS employee_count,

    AVG(e.salary) AS average_salary

FROM departments d

INNER JOIN employees e

    ON d.department_id = e.department_id

GROUP BY d.department_name

HAVING

    COUNT(e.employee_id) >= 2

    AND AVG(e.salary) > 60000;


-- =========================================================
-- END OF DAY 52
-- =========================================================
