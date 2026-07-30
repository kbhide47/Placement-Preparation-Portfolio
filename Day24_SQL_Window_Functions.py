-- ==========================================================
-- DAY 24 - SQL WINDOW FUNCTIONS
-- QUESTIONS + ANSWERS
-- ==========================================================


-- ==========================================================
-- Q1. Assign a row number to every employee based on salary
-- from highest to lowest.
-- ==========================================================

SELECT
    employee_id,
    employee_name,
    salary,
    ROW_NUMBER() OVER (
        ORDER BY salary DESC
    ) AS row_num
FROM employees;


-- ==========================================================
-- Q2. Rank employees based on salary.
-- ==========================================================

SELECT
    employee_name,
    salary,
    RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;


-- ==========================================================
-- Q3. Rank employees using DENSE_RANK().
-- ==========================================================

SELECT
    employee_name,
    salary,
    DENSE_RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;


-- ==========================================================
-- Q4. Compare ROW_NUMBER, RANK and DENSE_RANK.
-- ==========================================================

SELECT
    employee_name,
    salary,

    ROW_NUMBER() OVER (
        ORDER BY salary DESC
    ) AS row_number,

    RANK() OVER (
        ORDER BY salary DESC
    ) AS rank_number,

    DENSE_RANK() OVER (
        ORDER BY salary DESC
    ) AS dense_rank_number

FROM employees;


-- ==========================================================
-- Q5. Rank employees separately within each department.
-- ==========================================================

SELECT
    employee_name,
    department_id,
    salary,

    RANK() OVER (
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS department_rank

FROM employees;


-- ==========================================================
-- Q6. Find the highest-paid employee in each department.
-- ==========================================================

WITH ranked_employees AS (

    SELECT
        employee_name,
        department_id,
        salary,

        RANK() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS salary_rank

    FROM employees

)

SELECT *
FROM ranked_employees
WHERE salary_rank = 1;


-- ==========================================================
-- Q7. Find the second-highest salary in the company.
-- ==========================================================

WITH ranked_employees AS (

    SELECT
        employee_name,
        salary,

        DENSE_RANK() OVER (
            ORDER BY salary DESC
        ) AS salary_rank

    FROM employees

)

SELECT *
FROM ranked_employees
WHERE salary_rank = 2;


-- ==========================================================
-- Q8. Find the third-highest salary.
-- ==========================================================

WITH ranked_employees AS (

    SELECT
        employee_name,
        salary,

        DENSE_RANK() OVER (
            ORDER BY salary DESC
        ) AS salary_rank

    FROM employees

)

SELECT *
FROM ranked_employees
WHERE salary_rank = 3;


-- ==========================================================
-- Q9. Find the second-highest salary in every department.
-- ==========================================================

WITH ranked_employees AS (

    SELECT
        employee_name,
        department_id,
        salary,

        DENSE_RANK() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS salary_rank

    FROM employees

)

SELECT *
FROM ranked_employees
WHERE salary_rank = 2;


-- ==========================================================
-- Q10. Calculate average salary of each department
-- alongside every employee.
-- ==========================================================

SELECT
    employee_name,
    department_id,
    salary,

    AVG(salary) OVER (
        PARTITION BY department_id
    ) AS department_average_salary

FROM employees;


-- ==========================================================
-- Q11. Calculate the difference between employee salary
-- and department average salary.
-- ==========================================================

SELECT
    employee_name,
    department_id,
    salary,

    AVG(salary) OVER (
        PARTITION BY department_id
    ) AS department_average,

    salary -
    AVG(salary) OVER (
        PARTITION BY department_id
    ) AS difference_from_average

FROM employees;


-- ==========================================================
-- Q12. Calculate a running total of salaries.
-- ==========================================================

SELECT
    employee_name,
    salary,

    SUM(salary) OVER (
        ORDER BY employee_id
    ) AS running_total_salary

FROM employees;


-- ==========================================================
-- Q13. Find the previous employee's salary.
-- ==========================================================

SELECT
    employee_name,
    salary,

    LAG(salary) OVER (
        ORDER BY employee_id
    ) AS previous_salary

FROM employees;


-- ==========================================================
-- Q14. Find the next employee's salary.
-- ==========================================================

SELECT
    employee_name,
    salary,

    LEAD(salary) OVER (
        ORDER BY employee_id
    ) AS next_salary

FROM employees;


-- ==========================================================
-- Q15. Calculate salary difference from previous employee.
-- ==========================================================

SELECT
    employee_name,
    salary,

    LAG(salary) OVER (
        ORDER BY employee_id
    ) AS previous_salary,

    salary -
    LAG(salary) OVER (
        ORDER BY employee_id
    ) AS salary_difference

FROM employees;


-- ==========================================================
-- Q16. Find the highest-paid employee in each department
-- using ROW_NUMBER().
-- ==========================================================

WITH ranked_employees AS (

    SELECT
        employee_name,
        department_id,
        salary,

        ROW_NUMBER() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS row_num

    FROM employees

)

SELECT *
FROM ranked_employees
WHERE row_num = 1;


-- ==========================================================
-- Q17. Find top 2 employees from each department.
-- ==========================================================

WITH ranked_employees AS (

    SELECT
        employee_name,
        department_id,
        salary,

        ROW_NUMBER() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS row_num

    FROM employees

)

SELECT *
FROM ranked_employees
WHERE row_num <= 2;


-- ==========================================================
-- Q18. Calculate total salary of each department
-- without GROUP BY.
-- ==========================================================

SELECT
    employee_name,
    department_id,
    salary,

    SUM(salary) OVER (
        PARTITION BY department_id
    ) AS department_total_salary

FROM employees;


-- ==========================================================
-- Q19. Calculate percentage of department salary
-- contributed by each employee.
-- ==========================================================

SELECT
    employee_name,
    department_id,
    salary,

    SUM(salary) OVER (
        PARTITION BY department_id
    ) AS department_total_salary,

    ROUND(
        salary * 100.0 /
        SUM(salary) OVER (
            PARTITION BY department_id
        ),
        2
    ) AS salary_percentage

FROM employees;


-- ==========================================================
-- Q20. Display employee name, department name,
-- salary and department rank.
-- ==========================================================

SELECT
    e.employee_name,
    d.department_name,
    e.salary,

    RANK() OVER (
        PARTITION BY e.department_id
        ORDER BY e.salary DESC
    ) AS department_rank

FROM employees e

LEFT JOIN departments d
ON e.department_id = d.department_id;


-- ==========================================================
-- END OF DAY 24
-- ==========================================================
