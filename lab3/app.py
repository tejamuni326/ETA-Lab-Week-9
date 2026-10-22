import streamlit as st

st.set_page_config(page_title="Layouts", layout="wide")
st.title("Lab 3: Layouts")
st.sidebar.header("Sidebar Settings")
student = st.sidebar.text_input("Student name", "Teja")
view = st.sidebar.selectbox("Choose view", ["Overview", "Details"])

left, right = st.columns(2)
with left:
    st.subheader("Column One")
    st.info("This content is in the first column.")
with right:
    st.subheader("Column Two")
    st.success("This content is in the second column.")

tab1, tab2, tab3 = st.tabs(["Home", "Marks", "About"])
with tab1:
    st.write("Welcome to the Streamlit layout demo.")
with tab2:
    st.bar_chart({"Subject": ["Python", "Maths", "Data"], "Marks": [85, 78, 92]},
                 x="Subject", y="Marks")
with tab3:
    st.write("This app demonstrates sidebar, columns, tabs and containers.")

with st.container(border=True):
    st.write(f"Hello, {student}.")
    st.write("Selected view:", view)
