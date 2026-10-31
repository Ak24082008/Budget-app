import streamlit as st

st.title("✈️ Vacation Fund Tracker")

st.subheader("Monitor your trip allowance and expected costs")

st.markdown("---")

total_allowance = st.number_input(
    "Enter your total trip allowance ($):", 
    min_value=0.0, 
    value=1000.0, 
    step=50.0
)

st.write("### Anticipated Costs")

accommodation_cost = st.number_input(
    "Accommodation cost ($):", 
    min_value=0.0, 
    value=200.0, 
    step=10.0
)

flight_cost = st.number_input(
    "Flights & Travel ($):", 
    min_value=0.0, 
    value=100.0, 
    step=10.0
)

activities_cost = st.number_input(
    "Tours & Activities ($):", 
    min_value=0.0, 
    value=150.0, 
    step=10.0
)

if st.button("Analyze Trip Finances"):
    total_spent = accommodation_cost + flight_cost + activities_cost
    leftover_funds = total_allowance - total_spent
    
    st.markdown("---")
    
    st.write(f"**Total Estimated Costs:** ${total_spent:,.2f}")
    st.write(f"**Leftover Funds:** ${leftover_funds:,.2f}")
    
    buffer_zone = 0.20 * total_allowance
    
    if leftover_funds > buffer_zone:
        st.success("🌴 You are in the clear! Plenty of funds left for souvenirs and extras.")
        
    elif 0 <= leftover_funds <= buffer_zone:
        st.warning("⚠️ Heads up! Your travel funds are running tight. Spend carefully.")
        
    else:
        st.error("🛑 Over budget! You need to cut back on some trip costs before you travel.")