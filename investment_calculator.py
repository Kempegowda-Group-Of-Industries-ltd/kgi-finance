import streamlit as st

def investment_growth_calculator(conversion_rate):
    st.subheader("Investment Growth Calculator")

    principal = st.number_input("Initial Investment Amount", value=10000) * conversion_rate
    annual_rate = st.slider("Annual Interest Rate (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
    years = st.slider("Investment Duration (Years)", min_value=1, max_value=50, value=10)
    
    # Calculation
    future_value = principal * (1 + annual_rate / 100) ** years
    
    # Output results
    st.write(f"**Future Value**: {future_value/conversion_rate:.2f}")
