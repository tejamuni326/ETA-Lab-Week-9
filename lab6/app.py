import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Analyzer", layout="wide")
st.title("Lab 6: File Upload and Pandas")
uploaded = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded is not None:
    try:
        df = pd.read_csv(uploaded)
        st.success("CSV uploaded successfully.")
    except Exception as exc:
        st.error(f"Could not read the CSV: {exc}")
        st.stop()
else:
    st.info("Showing sample_data.csv because no file has been uploaded.")
    df = pd.read_csv("sample_data.csv")

st.subheader("Data preview")
st.dataframe(df.head(20), use_container_width=True)
c1, c2, c3 = st.columns(3)
c1.metric("Rows", len(df))
c2.metric("Columns", len(df.columns))
c3.metric("Missing cells", int(df.isna().sum().sum()))
st.subheader("Column summary")
st.write(pd.DataFrame({
    "Column": df.columns,
    "Data type": [str(x) for x in df.dtypes],
    "Missing values": [int(x) for x in df.isna().sum()]
}))
numeric = df.select_dtypes(include="number")
if not numeric.empty:
    st.subheader("Numeric summary")
    st.dataframe(numeric.describe(), use_container_width=True)
    column = st.selectbox("Choose a numeric column to chart", numeric.columns)
    st.bar_chart(df[column])
