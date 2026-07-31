import fitz

doc = fitz.open("data\resume.pdf")
for page in doc:
    text = page.get_text()
    print(text)