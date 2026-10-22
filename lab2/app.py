import streamlit as st

st.set_page_config(page_title="Widgets Playground", page_icon="🎛️")
st.title("Lab 2: Widgets Playground")
st.write("Try the different Streamlit input widgets.")

name = st.text_input("Name", "Teja")
about = st.text_area("About you", "I am learning Streamlit.")
age = st.number_input("Age", min_value=1, max_value=100, value=20)
rating = st.slider("Rate this lab", 1, 10, 7)
city = st.selectbox("Choose a city", ["Chennai", "Nayudupeta", "Bengaluru", "Hyderabad"])
skills = st.multiselect("Skills you want to learn", ["Python", "Pandas", "Streamlit", "Machine Learning"])
gender = st.radio("Study mode", ["Classroom", "Online"])
agree = st.checkbox("I have explored the widgets")
date = st.date_input("Choose a date")
color = st.color_picker("Choose a color", "#3366cc")
if st.button("Submit"):
    st.success(f"Submitted! Hello {name}.")
    st.write({"age": age, "rating": rating, "city": city, "skills": skills,
              "mode": gender, "agreed": agree, "date": str(date), "color": color})
st.write("About:", about)
