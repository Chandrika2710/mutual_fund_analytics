-- Top 5 Funds by Expense Ratio

SELECT scheme_name,
       expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct DESC
LIMIT 5;


-- Average NAV

SELECT AVG(nav) AS average_nav
FROM fact_nav;


-- Transaction Type Count

SELECT transaction_type,
       COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;


-- KYC Status Distribution

SELECT kyc_status,
       COUNT(*) AS total
FROM fact_transactions
GROUP BY kyc_status;


-- Risk Grade Distribution

SELECT risk_grade,
       COUNT(*) AS total
FROM fact_performance
GROUP BY risk_grade;