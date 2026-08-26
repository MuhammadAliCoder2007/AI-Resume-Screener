import fitz
import streamlit as st

from src.extract_reume import extract_resume
from src.preprocess import preprocess
from src.similarity import similarity
from src.scorer import score


st.title("AI Resume Screener")

st.write("Enter the job description and upload a resume to analyze.")

job_description = st.text_area(
    "Job Description",
    height=200
)

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)


if st.button("Analyze"):

    if job_description and resume:

        # Open uploaded PDF
        document = fitz.open(
            stream=resume.read(),
            filetype="pdf"
        )

        # Extract text from resume
        resume_text = extract_resume(document)

        # Preprocess both texts
        clean_job_description = preprocess(job_description)
        clean_resume = preprocess(resume_text)

        # Calculate similarity score
        similarity_score = similarity(
            clean_job_description,
            clean_resume
        )

        # Get match rating
        rating = score(similarity_score)

        # Display results
        st.subheader("Results")

        st.metric(
            "Resume Match Score",
            f"{similarity_score:.2f}%"
        )

        st.write(f"**Match Rating: {rating}**")

        st.progress(min(int(similarity_score), 100))

    else:
        st.warning(
            "Please enter both a job description and resume."
        )