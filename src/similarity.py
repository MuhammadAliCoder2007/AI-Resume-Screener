import fitz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from extract_reume import extract_resume

# Step 1: Load the job description and resume
def similarity(job_description, resume):

# Load the job description
    with open("data/job_description.txt", "r", encoding="utf-8") as f:
        job_text = f.read()

    # Load the resume
    document = fitz.open("data/resume.pdf")
    resume = extract_resume(document)

    # Step 2: Vectorize the job description and resume
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume,job_text])
    

    # Step 3: Calculate the similarity between the job description and resume
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    score = similarity[0][0]*100
    return score