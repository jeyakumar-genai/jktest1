import streamlit as st

st.title("🛒 Total Cost Calculator Including Tax")

# Input prices of 3 items
price1 = st.number_input("Enter price of item 1:", min_value=0.0, format="%.2f")
price2 = st.number_input("Enter price of item 2:", min_value=0.0, format="%.2f")
price3 = st.number_input("Enter price of item 3:", min_value=0.0, format="%.2f")

# Input tax percentage (e.g., enter 10 for 10%)
tax_percent = st.number_input("Enter tax percentage (%):", min_value=0.0, max_value=100.0, format="%.2f")

if st.button("Calculate Total Cost"):
    subtotal = price1 + price2 + price3
    tax_amount = subtotal * (tax_percent / 100)
    total = subtotal + tax_amount
    st.write(f"**Subtotal:** ${subtotal:,.2f}")
    st.write(f"**Tax Amount ({tax_percent}%):** ${tax_amount:,.2f}")
    st.success(f"**Total Cost including tax:** ${total:,.2f}")
