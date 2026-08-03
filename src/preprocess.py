import fitz
from extract_reume import extract_resume
document = fitz.open("data/resume.pdf")
text = extract_resume(document)
def preprocess(text):
    text = text.lower()
    text = text.replace("\n", " ")  # remove new lines
    text = text.replace("\r", " ")  # remove carriage returns
    text = text.replace("\t", " ")  # remove tabs
    text = text.replace("  ", " ")  # remove extra spaces
    text = "".join(char if char.isalnum() else " " for char in text)
    return text

print(preprocess(text))