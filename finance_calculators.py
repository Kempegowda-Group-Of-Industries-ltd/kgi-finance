import streamlit as st
from loan_calculator import loan_calculator
from auto_loan_calculator import auto_loan_calculator
from mortgage_calculator import mortgage_calculator
from retirement_calculator import retirement_calculator
from interest_payment_calculator import interest_payment_calculator
from compound_interest_calculator import compound_interest_calculator
from income_tax_calculator import income_tax_calculator
from investment_calculator import investment_growth_calculator
from amortization_calculator import amortization_calculator
from budget_tracker import budget_tracker
from inflation_calculator import inflation_calculator
from salary_calculator import salary_calculator
from sales_tax_calculator import sales_tax_calculator
from mortgage_payoff_calculator import mortgage_payoff_calculator
from k401_calculator import k401_calculator

st.title('Finance Calculators & Simulators')

# Sidebar to choose calculator type
app_mode = st.sidebar.selectbox("Choose the Calculator", 
                                ["Loan Calculator", "Auto Loan", "Mortgage Loan", "Retirement Calculator", 
                                 "Interest Payment", "Compound Interest", "Income Tax", 
                                 "Investment Growth", "Amortization", "Budget Tracker", 
                                 "Inflation Calculator", "Salary Calculator", "Sales Tax Calculator", 
                                 "Mortgage Payoff", "401K Calculator"])

# Global currency conversion settings
st.sidebar.header("Currency Settings")
currencies = {"USD": 1, "INR": 82.0}  # Example conversion rates
currency_choice = st.sidebar.selectbox("Select Currency", options=["USD", "INR"])
conversion_rate = currencies[currency_choice]

def display_calculator(app_mode, conversion_rate):
    if app_mode == "Loan Calculator":
        loan_calculator(conversion_rate)
    elif app_mode == "Auto Loan":
        auto_loan_calculator(conversion_rate)
    elif app_mode == "Mortgage Loan":
        mortgage_calculator(conversion_rate)
    elif app_mode == "Retirement Calculator":
        retirement_calculator(conversion_rate)
    elif app_mode == "Interest Payment":
        interest_payment_calculator(conversion_rate)
    elif app_mode == "Compound Interest":
        compound_interest_calculator(conversion_rate)
    elif app_mode == "Income Tax":
        income_tax_calculator(conversion_rate)
    elif app_mode == "Investment Growth":
        investment_growth_calculator(conversion_rate)
    elif app_mode == "Amortization":
        amortization_calculator(conversion_rate)
    elif app_mode == "Budget Tracker":
        budget_tracker(conversion_rate)
    elif app_mode == "Inflation Calculator":
        inflation_calculator(conversion_rate)
    elif app_mode == "Salary Calculator":
        salary_calculator(conversion_rate)
    elif app_mode == "Sales Tax Calculator":
        sales_tax_calculator(conversion_rate)
    elif app_mode == "Mortgage Payoff":
        mortgage_payoff_calculator(conversion_rate)
    elif app_mode == "401K Calculator":
        k401_calculator(conversion_rate)

# Display the selected calculator
display_calculator(app_mode, conversion_rate)
