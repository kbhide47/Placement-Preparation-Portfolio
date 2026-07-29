-- ==========================================================
-- DAY 23 - SUBQUERIES AND CTEs
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
    salary INT,
    experience INT
);

INSERT INTO employees VALUES
(1, 'Amit', 101, 60000, 2),
(2, 'Sneha', 102, 50000, 3),
(3, 'Rahul', 101, 80000, 5),
(4, 'Priya', 103, 70000, 4),
(5, 'Karan', NULL, 65000, 3),
(6, 'Neha', 102, 55000, 2),
(7, 'Rohan', 103, 75000, 5),
(8, 'Anjali', 101, 62000, 3);

-- ==========================================================
-- DAY 23 - SQL SUBQUERIES + CTEs
-- QUESTIONS + ANSWERS
-- ==========================================================


-- ==========================================================
-- Q1. Find employees earning more than the average salary.
-- ==========================================================

SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);


-- ==========================================================
-- Q2. Find the employee with the highest salary.
-- ==========================================================

SELECT *
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);


-- ==========================================================
-- Q3. Find the second-highest salary.
-- ==========================================================

SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
);


-- ==========================================================
-- Q4. Find employees earning the same salary as Rahul.
-- ==========================================================

SELECT *
FROM employees
WHERE salary = (
    SELECT salary
    FROM employees
    WHERE employee_name = 'Rahul'
);


-- ==========================================================
-- Q5. Find employees who earn more than Rahul.
-- ==========================================================

SELECT *
FROM employees
WHERE salary > (
    SELECT salary
    FROM employees
    WHERE employee_name = 'Rahul'
);


-- ==========================================================
-- Q6. Find employees working in the IT department.
-- Using a subquery instead of JOIN.
-- ==========================================================

SELECT *
FROM employees
WHERE department_id = (
    SELECT department_id
    FROM departments
    WHERE department_name = 'IT'
);


-- ==========================================================
-- Q7. Find employees working in IT or HR.
-- ==========================================================

SELECT *
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE department_name IN ('IT', 'HR')
);


-- ==========================================================
-- Q8. Find employees whose salary is greater than
-- the average salary of their department.
-- ==========================================================

SELECT
    e.employee_name,
    e.department_id,
    e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);


-- ==========================================================
-- Q9. Find the highest-paid employee in each department.
-- ==========================================================

SELECT
    e.employee_name,
    e.department_id,
    e.salary
FROM employees e
WHERE e.salary = (
    SELECT MAX(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);


-- ==========================================================
-- Q10. Find departments having at least 2 employees.
-- ==========================================================

SELECT
    department_id,
    COUNT(*) AS employee_count
FROM employees
WHERE department_id IS NOT NULL
GROUP BY department_id
HAVING COUNT(*) >= 2;


-- ==========================================================
-- Q11. Create a CTE to calculate average salary.
-- ==========================================================

WITH average_salary AS (

    SELECT
        AVG(salary) AS avg_salary
    FROM employees

)

SELECT *
FROM employees
WHERE salary > (
    SELECT avg_salary
    FROM average_salary
);


-- ==========================================================
-- Q12. Create a CTE for department salary statistics.
-- ==========================================================

WITH department_stats AS (

    SELECT
        department_id,
        AVG(salary) AS average_salary,
        MAX(salary) AS highest_salary,
        MIN(salary) AS lowest_salary
    FROM employees
    WHERE department_id IS NOT NULL
    GROUP BY department_id

)

SELECT *
FROM department_stats;


-- ==========================================================
-- Q13. Find departments where average salary > 65000.
-- Using CTE.
-- ==========================================================

WITH department_stats AS (

    SELECT
        department_id,
        AVG(salary) AS average_salary
    FROM employees
    WHERE department_id IS NOT NULL
    GROUP BY department_id

)

SELECT
    department_id,
    average_salary
FROM department_stats
WHERE average_salary > 65000;


-- ==========================================================
-- Q14. Use a CTE + JOIN to display department names
-- and average salary.
-- ==========================================================

WITH department_salary AS (

    SELECT
        department_id,
        AVG(salary) AS average_salary
    FROM employees
    WHERE department_id IS NOT NULL
    GROUP BY department_id

)

SELECT
    d.department_name,
    ds.average_salary
FROM department_salary ds
JOIN departments d
ON ds.department_id = d.department_id;


-- ==========================================================
-- Q15. Find employees earning above their department average.
-- Using CTE.
-- ==========================================================

WITH department_average AS (

    SELECT
        department_id,
        AVG(salary) AS average_salary
    FROM employees
    WHERE department_id IS NOT NULL
    GROUP BY department_id

)

SELECT
    e.employee_name,
    e.department_id,
    e.salary,
    da.average_salary
FROM employees e
JOIN department_average da
ON e.department_id = da.department_id
WHERE e.salary > da.average_salary;


-- ==========================================================
-- Q16. Find the department with the highest average salary.
-- ==========================================================

WITH department_average AS (

    SELECT
        department_id,
        AVG(salary) AS average_salary
    FROM employees
    WHERE department_id IS NOT NULL
    GROUP BY department_id

)

SELECT *
FROM department_average
WHERE average_salary = (
    SELECT MAX(average_salary)
    FROM department_average
);


-- ==========================================================
-- Q17. Find the third-highest salary using a subquery.
-- ==========================================================

SELECT MAX(salary) AS third_highest_salary
FROM employees
WHERE salary < (

    SELECT MAX(salary)
    FROM employees
    WHERE salary < (

        SELECT MAX(salary)
        FROM employees

    )

);


-- ==========================================================
-- Q18. Find employees whose salary is greater than
-- at least one employee in HR.
-- ==========================================================

SELECT *
FROM employees
WHERE salary > ANY (

    SELECT salary
    FROM employees
    WHERE department_id = (
        SELECT department_id
        FROM departments
        WHERE department_name = 'HR'
    )

);


-- ==========================================================
-- Q19. Find employees whose salary is greater than
-- every employee in HR.
-- ==========================================================

SELECT *
FROM employees
WHERE salary > ALL (

    SELECT salary
    FROM employees
    WHERE department_id = (
        SELECT department_id
        FROM departments
        WHERE department_name = 'HR'
    )

);

-- ==========================================================
-- Q20. Find employees whose department exists
-- in the departments table.
-- ==========================================================

SELECT *
FROM employees e
WHERE EXISTS (

    SELECT 1
    FROM departments d
    WHERE d.department_id = e.department_id

);


-- ==========================================================
-- END OF DAY 23
-- ==========================================================
