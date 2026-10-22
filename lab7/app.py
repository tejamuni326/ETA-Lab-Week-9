import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Lab 7: Interactive Sales Dashboard")
df = pd.read_csv("lab7/sales.csv", parse_dates=["Date"])

regions = st.sidebar.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
products = st.sidebar.multiselect("Product", sorted(df["Product"].unique()), default=sorted(df["Product"].unique()))
filtered = df[df["Region"].isin(regions) & df["Product"].isin(products)]

total_sales = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()
average_sales = filtered["Sales"].mean() if not filtered.empty else 0
a, b, c = st.columns(3)
a.metric("Total Sales", f"₹{total_sales:,.0f}")
b.metric("Total Profit", f"₹{total_profit:,.0f}")
c.metric("Average Sale", f"₹{average_sales:,.0f}")

if filtered.empty:
    st.warning("No records match the selected filters.")
else:
    left, right = st.columns(2)
    with left:
        st.subheader("Sales by Region")
        st.bar_chart(filtered.groupby("Region")["Sales"].sum())
    with right:
        st.subheader("Profit by Product")
        st.bar_chart(filtered.groupby("Product")["Profit"].sum())
    st.subheader("Sales records")
    st.dataframe(filtered, use_container_width=True)
