import streamlit as st

def loan_calculator(conversion_rate):
    st.subheader("Loan Calculator")
    
    principal = st.number_input("Loan Amount", value=10000) * conversion_rate
    annual_rate = st.slider("Annual Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
    years = st.slider("Loan Term (Years)", min_value=1, max_value=30, value=15)
    
    # Calculation
    monthly_rate = annual_rate / 100 / 12
    months = years * 12
    monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    total_payment = monthly_payment * months
    total_interest = total_payment - principal
    
    # Output results
    st.write(f"**Monthly Payment**: {monthly_payment/conversion_rate:.2f}")
    st.write(f"**Total Payment**: {total_payment/conversion_rate:.2f}")
    st.write(f"**Total Interest**: {total_interest/conversion_rate:.2f}")
