-- =========================================================
-- DAY 55 - ADVANCED SQL PLACEMENT PROBLEMS
-- =========================================================

CREATE DATABASE day55_advanced_sql;

USE day55_advanced_sql;


-- =========================================================
-- EMPLOYEES TABLE
-- =========================================================

CREATE TABLE employees (

    employee_id INT PRIMARY KEY,

    employee_name VARCHAR(50),

    department VARCHAR(50),

    salary INT,

    experience INT,

    manager_id INT

);


INSERT INTO employees
(employee_id, employee_name, department, salary, experience, manager_id)
VALUES

(1, 'Amit', 'IT', 60000, 2, 5),

(2, 'Riya', 'HR', 55000, 3, 6),

(3, 'Rahul', 'IT', 85000, 5, 5),

(4, 'Sneha', 'Finance', 50000, 2, 7),

(5, 'Karan', 'IT', 100000, 8, NULL),

(6, 'Priya', 'HR', 90000, 6, NULL),

(7, 'Arjun', 'Finance', 95000, 7, NULL),

(8, 'Neha', 'IT', 70000, 4, 5),

(9, 'Vikas', 'Finance', 65000, 3, 7),

(10, 'Ananya', 'HR', 75000, 5, 6);


-- =========================================================
-- DEPARTMENTS TABLE
-- =========================================================

CREATE TABLE departments (

    department_id INT PRIMARY KEY,

    department_name VARCHAR(50)

);


INSERT INTO departments
(department_id, department_name)
VALUES

(10, 'IT'),

(20, 'HR'),

(30, 'Finance'),

(40, 'Marketing');


-- =========================================================
-- Q1. Find employees earning more than
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
-- Q2. Find the second-highest salary.
-- =========================================================

SELECT MAX(salary) AS second_highest_salary

FROM employees

WHERE salary <

(
    SELECT MAX(salary)
    FROM employees
);


-- =========================================================
-- Q3. Find the second-highest-paid employee.
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
-- Q4. Find the highest-paid employee
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
        ) AS rn

    FROM employees
)

SELECT *

FROM ranked_employees

WHERE rn = 1;


-- =========================================================
-- Q5. Find the top 2 highest-paid employees
-- from each department.
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
        ) AS rn

    FROM employees
)

SELECT *

FROM ranked_employees

WHERE rn <= 2;


-- =========================================================
-- Q6. Find employees earning more than
-- their department's average salary.
-- =========================================================

SELECT *

FROM employees e

WHERE salary >

(
    SELECT AVG(e2.salary)

    FROM employees e2

    WHERE e2.department = e.department
);


-- =========================================================
-- Q7. Find the department with
-- the highest average salary.
-- =========================================================

SELECT

    department,

    AVG(salary) AS average_salary

FROM employees

GROUP BY department

ORDER BY average_salary DESC

LIMIT 1;


-- =========================================================
-- Q8. Find the department with
-- the second-highest average salary.
-- =========================================================

WITH department_salary AS
(
    SELECT

        department,

        AVG(salary) AS average_salary,

        DENSE_RANK() OVER
        (
            ORDER BY AVG(salary) DESC
        ) AS rnk

    FROM employees

    GROUP BY department
)

SELECT *

FROM department_salary

WHERE rnk = 2;


-- =========================================================
-- Q9. Find employees who earn
-- more than their manager.
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
-- Q10. Find the average salary
-- of each department.
-- =========================================================

SELECT

    department,

    AVG(salary) AS average_salary

FROM employees

GROUP BY department;


-- =========================================================
-- Q11. Find departments having
-- at least 3 employees.
-- =========================================================

SELECT

    department,

    COUNT(*) AS employee_count

FROM employees

GROUP BY department

HAVING COUNT(*) >= 3;


-- =========================================================
-- Q12. Find employees who have
-- the maximum salary in their department.
-- =========================================================

SELECT *

FROM employees e

WHERE salary =

(
    SELECT MAX(e2.salary)

    FROM employees e2

    WHERE e2.department = e.department
);


-- =========================================================
-- Q13. Rank all employees
-- based on salary.
-- =========================================================

SELECT

    employee_name,

    department,

    salary,

    DENSE_RANK() OVER
    (
        ORDER BY salary DESC
    ) AS salary_rank

FROM employees;


-- =========================================================
-- Q14. Rank employees within
-- their respective departments.
-- =========================================================

SELECT

    employee_name,

    department,

    salary,

    DENSE_RANK() OVER
    (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS department_rank

FROM employees;


-- =========================================================
-- Q15. Find the top 3 highest-paid
-- employees overall.
-- =========================================================

WITH ranked AS
(
    SELECT

        employee_name,

        salary,

        DENSE_RANK() OVER
        (
            ORDER BY salary DESC
        ) AS rnk

    FROM employees
)

SELECT *

FROM ranked

WHERE rnk <= 3;


-- =========================================================
-- Q16. Calculate running total of salaries.
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
-- Q17. Compare each employee's salary
-- with the previous employee's salary.
-- =========================================================

SELECT

    employee_name,

    salary,

    LAG(salary) OVER
    (
        ORDER BY employee_id
    ) AS previous_salary

FROM employees;


-- =========================================================
-- Q18. Find employees whose salary
-- is greater than the previous employee's salary.
-- =========================================================

WITH salary_comparison AS
(
    SELECT

        employee_name,

        salary,

        LAG(salary) OVER
        (
            ORDER BY employee_id
        ) AS previous_salary

    FROM employees
)

SELECT *

FROM salary_comparison

WHERE salary > previous_salary;


-- =========================================================
-- Q19. Find the highest-paid employee
-- in every department using CTE.
-- =========================================================

WITH department_rank AS
(
    SELECT

        employee_name,

        department,

        salary,

        ROW_NUMBER() OVER
        (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS rn

    FROM employees
)

SELECT

    employee_name,

    department,

    salary

FROM department_rank

WHERE rn = 1;


-- =========================================================
-- Q20. Find departments whose
-- average salary is greater than
-- the overall company average.
-- =========================================================

WITH department_average AS
(
    SELECT

        department,

        AVG(salary) AS avg_department_salary

    FROM employees

    GROUP BY department
)

SELECT *

FROM department_average

WHERE avg_department_salary >

(
    SELECT AVG(salary)
    FROM employees
);


-- =========================================================
-- END OF DAY 55
-- =========================================================
