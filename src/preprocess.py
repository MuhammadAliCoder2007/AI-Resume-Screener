import fitz # for pdf processing
from src.extract_reume import extract_resume # for extracting text from pdf
document = fitz.open("data/resume.pdf") # open the resume pdf
text = extract_resume(document) # extract the text from the resume pdf
def preprocess(text):
    text = text.lower()
    text = text.replace("\n", " ")  # remove new lines
    text = text.replace("\r", " ")  # remove carriage returns
    text = text.replace("\t", " ")  # remove tabs
    text = text.replace("  ", " ")  # remove extra spaces
    text = "".join(char if char.isalnum() else " " for char in text)
    return text

print(preprocess(text))