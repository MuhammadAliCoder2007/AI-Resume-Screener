# AI Resume Screener

An AI-powered tool that extracts text from PDF resumes and compares them with job descriptions to calculate a match score.

## Features

* PDF resume text extraction with PyMuPDF
* Text preprocessing
* Resume/job description similarity scoring
* Streamlit web interface

## Tech Stack

Python • Pandas • PyMuPDF • Scikit-learn • Streamlit

## Project Structure

```text
AI-Resume-Screener/
├── app/app.py
├── data/resume.pdf
├── models/
└── src/
    ├── extract_resume.py
    ├── preprocess.py
    ├── similarity.py
    └── scorer.py
```

## Run Locally

```bash
pip install pymupdf pandas streamlit scikit-learn
py -m streamlit run app/app.py
```

## Future Improvements

* TF-IDF and semantic similarity
* Skills extraction
* Keyword highlighting
* ATS compatibility scoring
* DOCX support

## License

MIT
