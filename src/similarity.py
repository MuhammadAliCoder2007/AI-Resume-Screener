import fitz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.extract_reume import extract_resume
from src.preprocess import preprocess

# Step 1: Load the job description and resume
def similarity(job_description, resume):

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform([resume, job_description])

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    score = similarity[0][0] * 100

    return score

with open("data/job_description.txt", "r", encoding="utf-8") as f:
    job_text = f.read()

document = fitz.open("data/resume.pdf")
resume_text = extract_resume(document)

job_text = preprocess(job_text)
resume_text = preprocess(resume_text)

print("Similarity:", similarity(job_text, resume_text))