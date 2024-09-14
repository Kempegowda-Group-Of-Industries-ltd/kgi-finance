import streamlit as st

def loan_calculator():
    st.header("Loan Calculator")

    # Input fields
    principal = st.number_input("Principal Amount ($)", min_value=0.0, format="%.2f")
    annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, format="%.2f")
    years = st.number_input("Term (Years)", min_value=1, format="%d")

    if st.button("Calculate"):
        # Calculations
        monthly_rate = annual_rate / 100 / 12
        number_of_payments = years * 12
        monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
        total_payment = monthly_payment * number_of_payments
        total_interest = total_payment - principal

        # Display results
        st.subheader("Results")
        st.write(f"Monthly Payment: ${monthly_payment:,.2f}")
        st.write(f"Total Payment: ${total_payment:,.2f}")
        st.write(f"Total Interest: ${total_interest:,.2f}")
