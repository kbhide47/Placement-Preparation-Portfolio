-- ==========================================================
-- DAY 22 - SQL JOINS
-- Create Tables
-- ==========================================================

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO departments VALUES
(101, 'IT'),
(102, 'HR'),
(103, 'Finance'),
(104, 'Marketing');


CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    salary INT
);

INSERT INTO employees VALUES
(1, 'Amit', 101, 60000),
(2, 'Sneha', 102, 50000),
(3, 'Rahul', 101, 80000),
(4, 'Priya', 103, 70000),
(5, 'Karan', NULL, 65000),
(6, 'Neha', 102, 55000),
(7, 'Rohan', 103, 75000),
(8, 'Anjali', 105, 62000);

-- ==========================================================
-- DAY 22 - SQL JOINS PRACTICE
-- ==========================================================

-- Q1. Display employee name with department name.

SELECT
    e.employee_name,
    d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;


-- Q2. Display all employees even if department is missing.

SELECT
    e.employee_name,
    d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;


-- Q3. Display all departments even if no employee works there.

SELECT
    d.department_name,
    e.employee_name
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id;


-- Q4. Display employees without any matching department.

SELECT
    e.employee_name,
    e.department_id
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id
WHERE d.department_id IS NULL;


-- Q5. Display departments without employees.

SELECT
    d.department_name
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.employee_id IS NULL;


-- Q6. Display employee name, department name and salary.

SELECT
    e.employee_name,
    d.department_name,
    e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;


-- Q7. Find employees earning more than 60000 with department names.

SELECT
    e.employee_name,
    d.department_name,
    e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
WHERE e.salary > 60000;


-- Q8. Count employees in each department.

SELECT
    d.department_name,
    COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;


-- Q9. Find average salary of each department.

SELECT
    d.department_name,
    AVG(e.salary) AS average_salary
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;


-- Q10. Find highest salary in each department.

SELECT
    d.department_name,
    MAX(e.salary) AS highest_salary
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;


-- Q11. Find employees working in IT department.

SELECT
    e.employee_name,
    e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
WHERE d.department_name = 'IT';


-- Q12. Find employees working in HR or Finance.

SELECT
    e.employee_name,
    d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
WHERE d.department_name IN ('HR', 'Finance');


-- Q13. Display employee names in ascending order with department names.

SELECT
    e.employee_name,
    d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
ORDER BY e.employee_name ASC;


-- Q14. Find total salary paid by each department.

SELECT
    d.department_name,
    SUM(e.salary) AS total_salary
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;


-- Q15. Display employee name and department name.
-- If department is missing, display 'Not Assigned'.

SELECT
    e.employee_name,
    COALESCE(d.department_name, 'Not Assigned') AS department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;

-- ==========================================================
-- END OF DAY 22
-- ==========================================================
