import os
import streamlit as st

from resume_parser import extract_resume_data
from gemini_client import get_resume_review
from utils import save_review

st.set_page_config(page_title="Resume Reviewer", page_icon="📄")

st.title("📄 AI Resume Reviewer")
st.write("Upload your resume (`.pdf` or `.docx`), and get instant feedback using Gemini AI.")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:
    # Save uploaded file to a temporary path
    temp_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())
    
    st.info("Extracting and parsing resume...")
    resume_data = extract_resume_data(temp_path)

    st.subheader("Parsed Resume Data")
    st.json(resume_data)

    if st.button("🔍 Get Gemini Review"):
        with st.spinner("Getting AI feedback..."):
            review = get_resume_review(resume_data)

        st.subheader("Gemini Review")
        st.text_area("Review", review, height=300)

        # Save review to file
        out_file = "review.json" if review.strip().startswith("{") else "review.txt"
        save_review(review, out_file)

        with open(out_file, "rb") as f:
            st.download_button(
                label="📥 Download Review",
                data=f,
                file_name=out_file,
                mime="application/json" if out_file.endswith(".json") else "text/plain"
            )

        # Cleanup
        os.remove(out_file)
        os.remove(temp_path)
