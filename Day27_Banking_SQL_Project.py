-- ==========================================================
-- DAY 26 - BANKING CUSTOMER & LOAN ANALYTICS
-- PART 2 - ADVANCED SQL INTERVIEW QUESTIONS
-- ==========================================================


-- ==========================================================
-- Q16. Find the top 5 branches with the highest loan amount.
-- ==========================================================

SELECT
    branch,
    SUM(loan_amount) AS total_loan_amount
FROM loans
GROUP BY branch
ORDER BY total_loan_amount DESC
LIMIT 5;


-- ==========================================================
-- Q17. Find customers having more than one loan.
-- ==========================================================

SELECT
    customer_id,
    COUNT(*) AS total_loans
FROM loans
GROUP BY customer_id
HAVING COUNT(*) > 1;


-- ==========================================================
-- Q18. Find the average credit score for each city.
-- ==========================================================

SELECT
    city,
    AVG(credit_score) AS average_credit_score
FROM customers
GROUP BY city
ORDER BY average_credit_score DESC;


-- ==========================================================
-- Q19. Find customers whose loan amount is greater than
-- their annual income.
-- ==========================================================

SELECT
    c.customer_name,
    c.annual_income,
    l.loan_amount
FROM customers c
INNER JOIN loans l
ON c.customer_id = l.customer_id
WHERE l.loan_amount > c.annual_income;


-- ==========================================================
-- Q20. Find customers with poor credit score (<600).
-- ==========================================================

SELECT
    customer_name,
    credit_score
FROM customers
WHERE credit_score < 600
ORDER BY credit_score;


-- ==========================================================
-- Q21. Find the customer with the highest loan amount.
-- ==========================================================

SELECT
    c.customer_name,
    l.loan_amount
FROM customers c
INNER JOIN loans l
ON c.customer_id = l.customer_id
WHERE l.loan_amount = (
    SELECT MAX(loan_amount)
    FROM loans
);


-- ==========================================================
-- Q22. Find the average loan amount for each occupation.
-- ==========================================================

SELECT
    c.occupation,
    AVG(l.loan_amount) AS average_loan
FROM customers c
INNER JOIN loans l
ON c.customer_id = l.customer_id
GROUP BY c.occupation
ORDER BY average_loan DESC;


-- ==========================================================
-- Q23. Find the highest loan amount in each branch.
-- ==========================================================

SELECT
    branch,
    MAX(loan_amount) AS highest_loan
FROM loans
GROUP BY branch;


-- ==========================================================
-- Q24. Rank customers based on loan amount.
-- ==========================================================

SELECT
    c.customer_name,
    l.loan_amount,

    DENSE_RANK() OVER (
        ORDER BY l.loan_amount DESC
    ) AS loan_rank

FROM customers c
INNER JOIN loans l
ON c.customer_id = l.customer_id;


-- ==========================================================
-- Q25. Find the second-highest loan amount.
-- ==========================================================

WITH ranked_loans AS (

    SELECT
        customer_id,
        loan_amount,

        DENSE_RANK() OVER (
            ORDER BY loan_amount DESC
        ) AS loan_rank

    FROM loans

)

SELECT *
FROM ranked_loans
WHERE loan_rank = 2;


-- ==========================================================
-- Q26. Find the highest loan in each branch.
-- ==========================================================

WITH ranked_branch_loans AS (

    SELECT
        customer_id,
        branch,
        loan_amount,

        ROW_NUMBER() OVER (
            PARTITION BY branch
            ORDER BY loan_amount DESC
        ) AS rn

    FROM loans

)

SELECT *
FROM ranked_branch_loans
WHERE rn = 1;


-- ==========================================================
-- Q27. Calculate the running total of loan amounts.
-- ==========================================================

SELECT
    loan_id,
    approval_date,
    loan_amount,

    SUM(loan_amount) OVER (
        ORDER BY approval_date
    ) AS running_total

FROM loans;


-- ==========================================================
-- Q28. Find each customer's contribution (%) to the
-- total loan amount.
-- ==========================================================

WITH customer_loans AS (

    SELECT
        customer_id,
        SUM(loan_amount) AS total_loan
    FROM loans
    GROUP BY customer_id

)

SELECT
    customer_id,
    total_loan,

    ROUND(
        total_loan * 100.0 /
        SUM(total_loan) OVER (),
        2
    ) AS contribution_percentage

FROM customer_loans
ORDER BY contribution_percentage DESC;


-- ==========================================================
-- Q29. Categorize customers based on credit score.
-- ==========================================================

SELECT
    customer_name,
    credit_score,

    CASE

        WHEN credit_score >= 750 THEN 'Excellent'

        WHEN credit_score >= 650 THEN 'Good'

        WHEN credit_score >= 600 THEN 'Average'

        ELSE 'Poor'

    END AS credit_category

FROM customers;


-- ==========================================================
-- Q30. Find customer name, loan amount, branch and
-- department rank by loan amount.
-- ==========================================================

SELECT
    c.customer_name,
    l.branch,
    l.loan_amount,

    RANK() OVER (
        PARTITION BY l.branch
        ORDER BY l.loan_amount DESC
    ) AS branch_rank

FROM customers c
INNER JOIN loans l
ON c.customer_id = l.customer_id;

-- ==========================================================
-- END OF DAY 26 - PART 2
-- ==========================================================
