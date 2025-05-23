import streamlit as st
import requests
import json

st.title("🧠 AI Candidate Screening Assistant")

st.subheader("Upload input.json or paste JSON")
input_mode = st.radio("Input Mode", ["Upload File", "Paste JSON"])

if input_mode == "Upload File":
    uploaded = st.file_uploader("Upload input.json", type=["json"])
    if uploaded:
        data = json.load(uploaded)
elif input_mode == "Paste JSON":
    json_input = st.text_area("Paste input JSON")
    if json_input:
        data = json.loads(json_input)

if 'data' in locals() and st.button("Screen Candidate"):
    response = requests.post("http://localhost:8000/screen", json=data)
    if response.status_code == 200:
        result = response.json()
        st.success("Evaluation complete!")
        st.write("**Score:**", result["score"])
        st.write("**Decision:**", result["decision"])
        st.write("**Explanation:**", result["explanation"])
    else:
        st.error("Error in API call")