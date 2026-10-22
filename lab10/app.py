import streamlit as st
import requests
import json

st.set_page_config(page_title="API Integration")
st.title("Lab 10: API Integration and JSON")
st.write("Fetch a sample post from JSONPlaceholder and inspect its JSON response.")

post_id = st.number_input("Post ID", min_value=1, max_value=100, value=1, step=1)
if st.button("Fetch API data"):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url, timeout=10)
        st.write("HTTP status:", response.status_code)
        response.raise_for_status()
        data = response.json()
        st.subheader("Formatted result")
        st.json(data)
        st.subheader("JSON string")
        st.code(json.dumps(data, indent=2), language="json")
    except requests.RequestException as exc:
        st.error(f"API request failed: {exc}")
else:
    st.info("Choose a post ID and click Fetch API data. Internet access is required.")
