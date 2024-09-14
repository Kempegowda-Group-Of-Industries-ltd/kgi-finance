import streamlit as st

def budget_tracker():
    st.header("Budget Tracker")

    # Input fields
    income = st.number_input("Monthly Income ($)", min_value=0.0, format="%.2f")
    rent = st.number_input("Rent/Mortgage ($)", min_value=0.0, format="%.2f")
    utilities = st.number_input("Utilities ($)", min_value=0.0, format="%.2f")
    groceries = st.number_input("Groceries ($)", min_value=0.0, format="%.2f")
    other_expenses = st.number_input("Other Expenses ($)", min_value=0.0, format="%.2f")

    if st.button("Calculate"):
        # Calculations
        total_expenses = rent + utilities + groceries + other_expenses
        remaining_balance = income - total_expenses

        # Display results
        st.subheader("Results")
        st.write(f"Total Expenses: ${total_expenses:,.2f}")
        st.write(f"Remaining Balance: ${remaining_balance:,.2f}")
