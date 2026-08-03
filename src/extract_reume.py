import fitz
document = fitz.open("data/resume.pdf")
def extract_resume(doc):
    text = ""    
    for page in doc:
        text += page.get_text()
    return text