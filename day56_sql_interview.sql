-- =========================================================
-- DAY 56 - SQL INTERVIEW CODING PRACTICE
-- =========================================================


-- =========================================================
-- SAMPLE TABLE
-- =========================================================

CREATE TABLE employees (

    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    experience INT,
    manager_id INT

);


-- =========================================================
-- Q1. Find the second-highest salary.
-- =========================================================

SELECT MAX(salary) AS second_highest_salary

FROM employees

WHERE salary <

(
    SELECT MAX(salary)
    FROM employees
);


-- =========================================================
-- Q2. Find the third-highest salary.
-- =========================================================

WITH ranked_salaries AS
(
    SELECT

        salary,

        DENSE_RANK() OVER
        (
            ORDER BY salary DESC
        ) AS salary_rank

    FROM employees
)

SELECT DISTINCT salary

FROM ranked_salaries

WHERE salary_rank = 3;


-- =========================================================
-- Q3. Find the highest-paid employee
-- in each department.
-- =========================================================

WITH ranked_employees AS
(
    SELECT

        employee_name,

        department,

        salary,

        DENSE_RANK() OVER
        (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS salary_rank

    FROM employees
)

SELECT *

FROM ranked_employees

WHERE salary_rank = 1;


-- =========================================================
-- Q4. Find the second-highest-paid employee
-- in each department.
-- =========================================================

WITH ranked_employees AS
(
    SELECT

        employee_name,

        department,

        salary,

        DENSE_RANK() OVER
        (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS salary_rank

    FROM employees
)

SELECT *

FROM ranked_employees

WHERE salary_rank = 2;


-- =========================================================
-- Q5. Find employees earning more than
-- the company average salary.
-- =========================================================

SELECT *

FROM employees

WHERE salary >

(
    SELECT AVG(salary)
    FROM employees
);


-- =========================================================
-- Q6. Find employees earning more than
-- their department average.
-- =========================================================

SELECT *

FROM employees e

WHERE salary >

(
    SELECT AVG(e2.salary)

    FROM employees e2

    WHERE e.department = e2.department
);


-- =========================================================
-- Q7. Find duplicate salaries.
-- =========================================================

SELECT

    salary,

    COUNT(*) AS count

FROM employees

GROUP BY salary

HAVING COUNT(*) > 1;


-- =========================================================
-- Q8. Find the top 3 highest-paid employees
-- in each department.
-- =========================================================

WITH ranked_employees AS
(
    SELECT

        employee_name,

        department,

        salary,

        ROW_NUMBER() OVER
        (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS row_num

    FROM employees
)

SELECT *

FROM ranked_employees

WHERE row_num <= 3;


-- =========================================================
-- Q9. Find employees earning more than
-- their manager.
-- =========================================================

SELECT

    e.employee_name AS employee,

    e.salary AS employee_salary,

    m.employee_name AS manager,

    m.salary AS manager_salary

FROM employees e

JOIN employees m

    ON e.manager_id = m.employee_id

WHERE e.salary > m.salary;


-- =========================================================
-- Q10. Calculate a running total of salaries.
-- =========================================================

SELECT

    employee_id,

    employee_name,

    salary,

    SUM(salary) OVER
    (
        ORDER BY employee_id
    ) AS running_total

FROM employees;


-- =========================================================
-- END OF DAY 56
-- =========================================================
