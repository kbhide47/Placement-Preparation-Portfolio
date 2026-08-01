-- ==========================================================
-- DAY 26 - BANKING CUSTOMER & LOAN ANALYTICS
-- PART 1 - FIRST 15 SQL INTERVIEW QUESTIONS
-- ==========================================================

-- Q1. Find the total number of customers.

SELECT COUNT(*) AS total_customers
FROM customers;


-- Q2. Find the total number of male and female customers.

SELECT
    gender,
    COUNT(*) AS total_customers
FROM customers
GROUP BY gender;


-- Q3. Find the average age of customers.

SELECT AVG(age) AS average_age
FROM customers;


-- Q4. Find the top 10 customers with the highest annual income.

SELECT
    customer_id,
    customer_name,
    annual_income
FROM customers
ORDER BY annual_income DESC
LIMIT 10;


-- Q5. Find customers having credit score greater than 750.

SELECT
    customer_id,
    customer_name,
    credit_score
FROM customers
WHERE credit_score > 750
ORDER BY credit_score DESC;


-- Q6. Find the total number of loans.

SELECT COUNT(*) AS total_loans
FROM loans;


-- Q7. Find the total loan amount approved by the bank.

SELECT SUM(loan_amount) AS total_loan_amount
FROM loans;


-- Q8. Find the average loan amount.

SELECT AVG(loan_amount) AS average_loan_amount
FROM loans;


-- Q9. Find total loan amount for each loan type.

SELECT
    loan_type,
    SUM(loan_amount) AS total_loan_amount
FROM loans
GROUP BY loan_type
ORDER BY total_loan_amount DESC;


-- Q10. Find total loan amount approved by each branch.

SELECT
    branch,
    SUM(loan_amount) AS total_loan_amount
FROM loans
GROUP BY branch
ORDER BY total_loan_amount DESC;


-- Q11. Find the number of approved and rejected loans.

SELECT
    loan_status,
    COUNT(*) AS total_loans
FROM loans
GROUP BY loan_status;


-- Q12. Find the loan approval percentage.

SELECT
    ROUND(
        SUM(CASE
                WHEN loan_status = 'Approved' THEN 1
                ELSE 0
            END) * 100.0 / COUNT(*),
        2
    ) AS approval_percentage
FROM loans;


-- Q13. Find the highest loan amount.

SELECT MAX(loan_amount) AS highest_loan
FROM loans;


-- Q14. Find customer name along with loan amount and loan type.

SELECT
    c.customer_name,
    l.loan_type,
    l.loan_amount
FROM customers c
INNER JOIN loans l
ON c.customer_id = l.customer_id;


-- Q15. Find customers whose loan amount is greater than ₹5,00,000.

SELECT
    c.customer_name,
    l.loan_amount
FROM customers c
INNER JOIN loans l
ON c.customer_id = l.customer_id
WHERE l.loan_amount > 500000
ORDER BY l.loan_amount DESC;

-- ==========================================================
-- END OF DAY 26 - PART 1
-- ==========================================================
