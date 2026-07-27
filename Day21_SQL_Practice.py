CREATE TABLE employees (
    employee_id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    experience INT,
    city VARCHAR(50)
);

INSERT INTO employees VALUES
(1, 'Amit', 'IT', 60000, 2, 'Pune'),
(2, 'Sneha', 'HR', 50000, 3, 'Mumbai'),
(3, 'Rahul', 'IT', 80000, 5, 'Pune'),
(4, 'Priya', 'Finance', 70000, 4, 'Delhi'),
(5, 'Karan', 'IT', 90000, 6, 'Mumbai'),
(6, 'Neha', 'HR', 55000, 2, 'Pune'),
(7, 'Rohan', 'Finance', 75000, 5, 'Mumbai'),
(8, 'Anjali', 'IT', 65000, 3, 'Delhi');

-- ==========================================================
-- DAY 21 - SQL PRACTICE
-- PART 2: QUESTIONS + ANSWERS
-- ==========================================================


-- Q1. Display all employees.

SELECT *
FROM employees;


-- Q2. Display only name, department and salary.

SELECT name, department, salary
FROM employees;


-- Q3. Find employees earning more than 70000.

SELECT *
FROM employees
WHERE salary > 70000;


-- Q4. Find employees from IT department.

SELECT *
FROM employees
WHERE department = 'IT';


-- Q5. Sort employees by salary from highest to lowest.

SELECT *
FROM employees
ORDER BY salary DESC;


-- Q6. Find the average salary of all employees.

SELECT AVG(salary) AS average_salary
FROM employees;


-- Q7. Find maximum and minimum salary.

SELECT
    MAX(salary) AS maximum_salary,
    MIN(salary) AS minimum_salary
FROM employees;


-- Q8. Find average salary by department.

SELECT
    department,
    AVG(salary) AS average_salary
FROM employees
GROUP BY department;


-- Q9. Find departments having average salary greater than 65000.

SELECT
    department,
    AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 65000;


-- Q10. Categorize employees based on salary.

SELECT
    name,
    salary,
    CASE
        WHEN salary >= 80000 THEN 'High'
        WHEN salary >= 60000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category
FROM employees;


-- Q11. Find employees having experience greater than 3 years
-- AND salary above 70000.

SELECT *
FROM employees
WHERE experience > 3
AND salary > 70000;


-- Q12. Find the second-highest salary.

SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
);


-- Q13. Find employees earning more than the average salary.

SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);


-- Q14. Count employees in each department.

SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department;


-- Q15. Find the highest-paid employee in each department.

SELECT
    department,
    MAX(salary) AS highest_salary
FROM employees
GROUP BY department;


-- ==========================================================
-- END OF DAY 21 PART 2
-- ==========================================================
