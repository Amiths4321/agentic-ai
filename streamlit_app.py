import streamlit as st
import requests

API_URL = "http://localhost:8000/analyze"

st.title("🤖 DevOps AI Agent (FREE)")

log = st.text_area("Paste logs here", height=200)

if st.button("Analyze"):
    try:
        res = requests.post(API_URL, json={"log": log})

        st.write("Status:", res.status_code)

        data = res.json()

        st.success("Analysis Complete")
        st.write(data["response"])

    except Exception as e:
        st.error("Error")
        st.text(str(e))