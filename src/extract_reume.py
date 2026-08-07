import fitz# for pdf processing
document = fitz.open("data/resume.pdf") # open the resume pdf
def extract_resume(doc): # extract the text from the resume pdf
    text = "" # initialize the text
    for page in doc: # iterate through the pages
        text += page.get_text() # get the text from the page
    return text # return the text