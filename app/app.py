#how well does the resume match the job description
#what skills are missing
#how can the candinate improve the resume

import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Analyze Resume for Job Description")
st.write("Enter the job description and resume to analyze: ")

job_description = st.text_area("Job Description", height=200)
resume = st.file_uploader("Upload Resume", type=["pdf", "docx", "doc"])

if st.button("Analyze"):
    if job_description and resume:
        st.write("Analyzing...")
    else:
        st.write("Please enter both job description and resume")
