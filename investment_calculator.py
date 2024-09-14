import streamlit as st

def investment_growth():
    st.header("Investment Growth Calculator")

    # Input fields
    initial_investment = st.number_input("Initial Investment ($)", min_value=0.0, format="%.2f")
    annual_return = st.number_input("Annual Return Rate (%)", min_value=0.0, format="%.2f")
    years = st.number_input("Number of Years", min_value=1, format="%d")

    if st.button("Calculate"):
        # Calculations
        future_value = initial_investment * ((1 + annual_return / 100) ** years)
        total_earned = future_value - initial_investment

        # Display results
        st.subheader("Results")
        st.write(f"Future Value: ${future_value:,.2f}")
        st.write(f"Total Earned: ${total_earned:,.2f}")
