CREATE TABLE fact_nav (
    amfi_code INTEGER,
    nav_date DATE,
    nav REAL
);

CREATE TABLE fact_transactions (
    investor_id TEXT,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT
);

CREATE TABLE fact_performance (
    amfi_code INTEGER,
    scheme_name TEXT,
    fund_house TEXT,
    expense_ratio_pct REAL,
    morningstar_rating INTEGER,
    risk_grade TEXT
);