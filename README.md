# AI Resume Screener

An AI-powered resume screening tool that extracts text from PDF resumes and compares them against job descriptions to determine how well a candidate matches a position.

## Features

- Extracts text from PDF resumes using PyMuPDF
- Cleans and preprocesses extracted text
- Compares resumes with job descriptions
- Calculates a resume match score
- Displays results in a simple Streamlit web application

## Tech Stack

- Python
- Pandas
- PyMuPDF (fitz)
- Streamlit

## Project Structure

```
AI-Resume-Screener/
│
├── app/
│   └── app.py                 # Streamlit interface
│
├── data/
│   └── resume.pdf             # Sample resume
│
├── models/
│
├── src/
│   ├── extract_resume.py      # Extract text from PDF
│   ├── preprocess.py          # Clean extracted text
│   ├── similarity.py          # Resume/job description comparison
│   └── scorer.py              # Final resume score
│
├── .gitignore
└── README.md
```

## How It Works

1. Upload a resume PDF.
2. Extract text from the document.
3. Clean and preprocess the text.
4. Compare the resume with a job description.
5. Calculate a similarity score.
6. Display the final match percentage.

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Resume-Screener.git
cd AI-Resume-Screener
```

Install dependencies:

```bash
pip install pymupdf pandas streamlit scikit-learn
```

Run the application:

```bash
py -m streamlit run app/app.py
```

## Future Improvements

- TF-IDF similarity scoring
- Keyword highlighting
- Resume ranking for multiple applicants
- NLP-based semantic similarity
- Support for DOCX resumes
- Skills extraction
- ATS compatibility scoring

## Learning Goals

This project was built to practice:

- PDF parsing
- Text preprocessing
- Natural Language Processing fundamentals
- Python project organization
- Streamlit application development
- Building portfolio-ready machine learning projects

## License

This project is licensed under the MIT License.
