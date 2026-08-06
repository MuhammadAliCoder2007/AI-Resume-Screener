import fitz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from extract_reume import extract_resume



with open("data/job_description.txt", "r", encoding="utf-8") as f:
    job_text = f.read()
document = fitz.open("data/resume.pdf")
resume = extract_resume(document)
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([resume,job_text])


similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
print(f"Similarity: {similarity[0][0]*100:.2f}%")