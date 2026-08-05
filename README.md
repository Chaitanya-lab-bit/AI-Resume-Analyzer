# AI Resume Analyzer

A Python-based AI Resume Analyzer that compares resumes with job descriptions and calculates an ATS (Applicant Tracking System) score.

## Features

- Resume PDF Parsing
- Job Description Analysis
- ATS Score Calculation
- Skill Matching
- Missing Skill Detection
- Resume Rating
- Recommendations
- PDF Report Generation

## Technologies Used

- Python
- pdfplumber
- reportlab
- Regular Expressions (re)
- Tkinter (File Picker)

## Project Structure

AI_Resume_Analyzer/
├── main.py
├── parser.py
├── analyzer.py
├── report.py
├── resumes/
├── job_descriptions/
├── reports/
├── requirements.txt
└── README.md

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

## Future Improvements

- AI-based resume suggestions
- NLP-based keyword extraction
- Web interface using Flask
- Multiple resume comparison