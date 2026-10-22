import streamlit as st

st.set_page_config(page_title="Forms and State")
st.title("Lab 4: Forms and Session State")

if "submissions" not in st.session_state:
    st.session_state.submissions = []

with st.form("student_form"):
    name = st.text_input("Student name")
    course = st.selectbox("Course", ["Computing and Data Science", "AI & ML", "Full Stack"])
    score = st.number_input("Score", min_value=0, max_value=100, value=75)
    submitted = st.form_submit_button("Save details")

if submitted:
    if name.strip():
        st.session_state.submissions.append(
            {"Name": name.strip(), "Course": course, "Score": score}
        )
        st.success("Details saved for this session.")
    else:
        st.warning("Please enter a student name.")

st.subheader("Saved submissions")
if st.session_state.submissions:
    st.dataframe(st.session_state.submissions, use_container_width=True)
else:
    st.info("Submit the form to see records here.")
if st.button("Clear records"):
    st.session_state.submissions = []
    st.rerun()
