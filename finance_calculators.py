import streamlit as st
from loan_calculator import loan_calculator
from investment_calculator import investment_growth
from budget_tracker import budget_tracker

def main():
    st.title('Finance Calculators & Simulators')

    # Sidebar to choose calculator type
    app_mode = st.sidebar.selectbox(
        "Choose the Calculator", 
        ["Loan Calculator", "Investment Growth", "Budget Tracker"]
    )

    # Display the selected module
    if app_mode == "Loan Calculator":
        loan_calculator()
    elif app_mode == "Investment Growth":
        investment_growth()
    elif app_mode == "Budget Tracker":
        budget_tracker()

if __name__ == "__main__":
    main()
