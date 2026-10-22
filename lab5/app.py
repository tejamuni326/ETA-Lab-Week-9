import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Visualization", layout="wide")
st.title("Lab 5: Data Visualization")
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 135, 180, 210, 195],
    "Expenses": [80, 95, 90, 110, 130, 125],
    "Visitors": [500, 620, 580, 700, 810, 760]
})
st.subheader("Sample data")
st.dataframe(df, use_container_width=True)
left, right = st.columns(2)
with left:
    st.subheader("Monthly Sales")
    st.line_chart(df.set_index("Month")[["Sales"]])
with right:
    st.subheader("Sales and Expenses")
    st.bar_chart(df.set_index("Month")[["Sales", "Expenses"]])
st.subheader("Visitors")
st.area_chart(df.set_index("Month")[["Visitors"]])
