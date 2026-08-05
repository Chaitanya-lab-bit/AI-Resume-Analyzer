from parser import read_resume, read_job_description, extract_details
from analyzer import (
    extract_skills,
    compare_skills,
    calculate_ats,
    resume_rating,
    get_recommendations
)
from report import generate_report

from tkinter import Tk
from tkinter.filedialog import askopenfilename

# -------------------------------
# Select Resume PDF
# -------------------------------
Tk().withdraw()

print("Select Resume PDF")

resume_path = askopenfilename(
    title="Select Resume PDF",
    filetypes=[("PDF Files", "*.pdf")]
)

# Check if no file selected
if not resume_path:
    print("No resume selected.")
    exit()

# -------------------------------
# Job Description File
# -------------------------------
job_path = "job_descriptions/job_descriptions.txt"

# -------------------------------
# Read Files
# -------------------------------
resume_text = read_resume(resume_path)
job_text = read_job_description(job_path)

if resume_text is None or job_text is None:
    print("Error reading files.")
    exit()

# -------------------------------
# Extract Candidate Details
# -------------------------------
name, email, phone = extract_details(resume_text)

# -------------------------------
# Extract Skills
# -------------------------------
resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(job_text)

# -------------------------------
# Compare Skills
# -------------------------------
matched, missing = compare_skills(resume_skills, jd_skills)

# -------------------------------
# ATS Score
# -------------------------------
ats_score = calculate_ats(matched, len(jd_skills))

# -------------------------------
# Rating & Recommendations
# -------------------------------
rating = resume_rating(ats_score)
recommendations = get_recommendations(missing)

# -------------------------------
# Display Results
# -------------------------------
print("\n========== AI RESUME ANALYZER ==========\n")

print("Candidate Details")
print("----------------------------")
print("Name :", name)
print("Email:", email)
print("Phone:", phone)

print("\nResume Skills")
print("----------------------------")
for skill in resume_skills:
    print("✔", skill)

print("\nJob Description Skills")
print("----------------------------")
for skill in jd_skills:
    print("✔", skill)

print("\nMatched Skills")
print("----------------------------")
for skill in matched:
    print("✔", skill)

print("\nMissing Skills")
print("----------------------------")
for skill in missing:
    print("✘", skill)

print(f"\nATS Score : {ats_score}%")
print("Resume Rating :", rating)

print("\nRecommendations")
print("----------------------------")
for rec in recommendations:
    print("•", rec)

# -------------------------------
# Generate PDF Report
# -------------------------------
generate_report(
    name,
    ats_score,
    matched,
    missing,
    rating,
    recommendations
)

print("\nPDF Report Generated Successfully!")
print("Saved in reports/ATS_Report.pdf")