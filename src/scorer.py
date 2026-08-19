from src.similarity import similarity
from src.extract_reume import extract_resume
from src.preprocess import preprocess
import fitz

def score(resume, job_description):
    result = similarity(job_description, resume)

    if result < 50:
        return "The resume is not a good fit for the job description"
    elif result < 70:
        return "The resume is a good fit for the job description"
    else:
        return "The resume is a great fit for the job description"
with open("data/job_description.txt", "r", encoding="utf-8") as f:
    job_text = f.read()
document = fitz.open("data/resume.pdf")
resume_text = extract_resume(document)

job_text = preprocess(job_text)
resume_text = preprocess(resume_text)

score = score(resume_text, job_text)
print(score)