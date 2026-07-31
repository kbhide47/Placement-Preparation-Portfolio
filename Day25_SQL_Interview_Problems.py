-- ==========================================================
-- DAY 25 - ADVANCED SQL INTERVIEW PRACTICE
-- ==========================================================


-- ==========================================================
-- DATASET
-- ==========================================================

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    employee_name VARCHAR(50),
    department VARCHAR(50),
    sale_date DATE,
    product VARCHAR(50),
    amount INT
);


INSERT INTO sales VALUES
(1, 101, 'Amit',   'IT',      '2026-01-05', 'Laptop',   80000),
(2, 102, 'Sneha',  'HR',      '2026-01-10', 'Monitor',  30000),
(3, 103, 'Rahul',  'IT',      '2026-01-15', 'Laptop',   90000),
(4, 104, 'Priya',  'Finance', '2026-01-20', 'Monitor',  40000),
(5, 101, 'Amit',   'IT',      '2026-02-05', 'Phone',    50000),
(6, 102, 'Sneha',  'HR',      '2026-02-10', 'Laptop',   70000),
(7, 103, 'Rahul',  'IT',      '2026-02-15', 'Phone',    60000),
(8, 104, 'Priya',  'Finance', '2026-02-20', 'Laptop',   85000),
(9, 105, 'Karan',  'IT',      '2026-02-25', 'Monitor',  45000),
(10, 106, 'Neha',  'HR',      '2026-03-05', 'Phone',    55000),
(11, 103, 'Rahul',  'IT',      '2026-03-10', 'Laptop',  100000),
(12, 105, 'Karan',  'IT',      '2026-03-15', 'Phone',    65000),
(13, 101, 'Amit',   'IT',      '2026-03-20', 'Monitor',  35000),
(14, 104, 'Priya', 'Finance',  '2026-03-25', 'Phone',    70000),
(15, 106, 'Neha',  'HR',      '2026-03-28', 'Laptop',   75000);


-- ==========================================================
-- Q1. Find total sales.
-- ==========================================================

SELECT
    SUM(amount) AS total_sales
FROM sales;


-- ==========================================================
-- Q2. Find total sales by employee.
-- ==========================================================

SELECT
    employee_id,
    employee_name,
    SUM(amount) AS total_sales
FROM sales
GROUP BY employee_id, employee_name
ORDER BY total_sales DESC;


-- ==========================================================
-- Q3. Find the employee with the highest total sales.
-- ==========================================================

WITH employee_sales AS (

    SELECT
        employee_id,
        employee_name,
        SUM(amount) AS total_sales
    FROM sales
    GROUP BY employee_id, employee_name

),

ranked AS (

    SELECT
        *,
        DENSE_RANK() OVER (
            ORDER BY total_sales DESC
        ) AS sales_rank
    FROM employee_sales

)

SELECT *
FROM ranked
WHERE sales_rank = 1;


-- ==========================================================
-- Q4. Find average sale amount for each department.
-- ==========================================================

SELECT
    department,
    AVG(amount) AS average_sale
FROM sales
GROUP BY department;


-- ==========================================================
-- Q5. Find departments whose total sales exceed 200000.
-- ==========================================================

SELECT
    department,
    SUM(amount) AS total_sales
FROM sales
GROUP BY department
HAVING SUM(amount) > 200000;


-- ==========================================================
-- Q6. Find employees whose total sales are greater
-- than the average employee sales.
-- ==========================================================

WITH employee_sales AS (

    SELECT
        employee_id,
        employee_name,
        SUM(amount) AS total_sales
    FROM sales
    GROUP BY employee_id, employee_name

)

SELECT *
FROM employee_sales
WHERE total_sales > (
    SELECT AVG(total_sales)
    FROM employee_sales
);


-- ==========================================================
-- Q7. Find highest-selling employee in each department.
-- ==========================================================

WITH employee_sales AS (

    SELECT
        employee_id,
        employee_name,
        department,
        SUM(amount) AS total_sales
    FROM sales
    GROUP BY
        employee_id,
        employee_name,
        department

),

ranked AS (

    SELECT
        *,
        DENSE_RANK() OVER (
            PARTITION BY department
            ORDER BY total_sales DESC
        ) AS sales_rank
    FROM employee_sales

)

SELECT *
FROM ranked
WHERE sales_rank = 1;


-- ==========================================================
-- Q8. Find second-highest-selling employee
-- in each department.
-- ==========================================================

WITH employee_sales AS (

    SELECT
        employee_id,
        employee_name,
        department,
        SUM(amount) AS total_sales
    FROM sales
    GROUP BY
        employee_id,
        employee_name,
        department

),

ranked AS (

    SELECT
        *,
        DENSE_RANK() OVER (
            PARTITION BY department
            ORDER BY total_sales DESC
        ) AS sales_rank
    FROM employee_sales

)

SELECT *
FROM ranked
WHERE sales_rank = 2;


-- ==========================================================
-- Q9. Find top 2 employees overall based on total sales.
-- ==========================================================

WITH employee_sales AS (

    SELECT
        employee_id,
        employee_name,
        SUM(amount) AS total_sales
    FROM sales
    GROUP BY employee_id, employee_name

),

ranked AS (

    SELECT
        *,
        DENSE_RANK() OVER (
            ORDER BY total_sales DESC
        ) AS sales_rank
    FROM employee_sales

)

SELECT *
FROM ranked
WHERE sales_rank <= 2;


-- ==========================================================
-- Q10. Find monthly sales.
-- ==========================================================

SELECT
    EXTRACT(YEAR FROM sale_date) AS year,
    EXTRACT(MONTH FROM sale_date) AS month,
    SUM(amount) AS monthly_sales
FROM sales
GROUP BY
    EXTRACT(YEAR FROM sale_date),
    EXTRACT(MONTH FROM sale_date)
ORDER BY year, month;


-- ==========================================================
-- Q11. Find the month with the highest sales.
-- ==========================================================

WITH monthly_sales AS (

    SELECT
        EXTRACT(YEAR FROM sale_date) AS year,
        EXTRACT(MONTH FROM sale_date) AS month,
        SUM(amount) AS total_sales
    FROM sales
    GROUP BY
        EXTRACT(YEAR FROM sale_date),
        EXTRACT(MONTH FROM sale_date)

),

ranked AS (

    SELECT
        *,
        DENSE_RANK() OVER (
            ORDER BY total_sales DESC
        ) AS sales_rank
    FROM monthly_sales

)

SELECT *
FROM ranked
WHERE sales_rank = 1;


-- ==========================================================
-- Q12. Calculate running total of sales by date.
-- ==========================================================

SELECT
    sale_date,
    amount,

    SUM(amount) OVER (
        ORDER BY sale_date
        ROWS BETWEEN UNBOUNDED PRECEDING
        AND CURRENT ROW
    ) AS running_total

FROM sales
ORDER BY sale_date;


-- ==========================================================
-- Q13. Calculate month-over-month sales change.
-- ==========================================================

WITH monthly_sales AS (

    SELECT
        EXTRACT(YEAR FROM sale_date) AS year,
        EXTRACT(MONTH FROM sale_date) AS month,
        SUM(amount) AS total_sales
    FROM sales
    GROUP BY
        EXTRACT(YEAR FROM sale_date),
        EXTRACT(MONTH FROM sale_date)

),

previous_month AS (

    SELECT
        year,
        month,
        total_sales,

        LAG(total_sales) OVER (
            ORDER BY year, month
        ) AS previous_sales

    FROM monthly_sales

)

SELECT
    year,
    month,
    total_sales,
    previous_sales,

    total_sales - previous_sales
        AS sales_change

FROM previous_month;


-- ==========================================================
-- Q14. Find each employee's percentage contribution
-- to total company sales.
-- ==========================================================

WITH employee_sales AS (

    SELECT
        employee_id,
        employee_name,
        SUM(amount) AS total_sales
    FROM sales
    GROUP BY employee_id, employee_name

)

SELECT
    employee_name,
    total_sales,

    ROUND(
        total_sales * 100.0 /
        SUM(total_sales) OVER (),
        2
    ) AS percentage_of_total_sales

FROM employee_sales
ORDER BY total_sales DESC;


-- ==========================================================
-- Q15. Find the highest-selling product.
-- ==========================================================

WITH product_sales AS (

    SELECT
        product,
        SUM(amount) AS total_sales
    FROM sales
    GROUP BY product

),

ranked AS (

    SELECT
        *,
        DENSE_RANK() OVER (
            ORDER BY total_sales DESC
        ) AS sales_rank
    FROM product_sales

)

SELECT *
FROM ranked
WHERE sales_rank = 1;


-- ==========================================================
-- END OF DAY 25
-- ==========================================================
