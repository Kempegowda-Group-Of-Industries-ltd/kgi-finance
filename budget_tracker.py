import streamlit as st
import pandas as pd

def budget_tracker(conversion_rate):
    st.subheader("Budget Tracker")

    st.write("Enter your income and expenses to track your budget.")

    income = st.number_input("Monthly Income", value=3000) * conversion_rate
    expenses = {
        "Rent": st.number_input("Rent", value=1000) * conversion_rate,
        "Utilities": st.number_input("Utilities", value=200) * conversion_rate,
        "Groceries": st.number_input("Groceries", value=300) * conversion_rate,
        "Other": st.number_input("Other Expenses", value=400) * conversion_rate
    }

    total_expenses = sum(expenses.values())
    remaining_budget = income - total_expenses

    # Display results
    st.write(f"**Total Expenses**: {total_expenses/conversion_rate:.2f}")
    st.write(f"**Remaining Budget**: {remaining_budget/conversion_rate:.2f}")
