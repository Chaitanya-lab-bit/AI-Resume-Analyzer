from parser import ResumeParser
from analyzer import ResumeAnalyzer
from report import generate_report
from resume import Resume

from tkinter import Tk
from tkinter.filedialog import askopenfilename

# -------------------------
# Create Objects
# -------------------------
parser = ResumeParser()
analyzer = ResumeAnalyzer()

# -------------------------
# Select Resume PDF
# -------------------------
Tk().withdraw()

print("Select Resume PDF")

resume_path = askopenfilename(
    title="Select Resume PDF",
    filetypes=[("PDF Files", "*.pdf")]
)

if not resume_path:
    print("No Resume Selected.")
    exit()

# -------------------------
# Job Description File
# -------------------------
job_path = "job_descriptions/job_descriptions.txt"

# -------------------------
# Read Files
# -------------------------
resume_text = parser.read_resume(resume_path)
job_text = parser.read_job_description(job_path)

if resume_text is None or job_text is None:
    print("Error reading files.")
    exit()

# -------------------------
# Extract Candidate Details
# -------------------------
name, email, phone = parser.extract_details(resume_text)

# -------------------------
# OOP Object
# -------------------------
candidate = Resume(name, email, phone)
candidate.display()

# -------------------------
# Extract Skills
# -------------------------
resume_skills = analyzer.extract_skills(resume_text)
jd_skills = analyzer.extract_skills(job_text)

# -------------------------
# Compare Skills
# -------------------------
matched, missing = analyzer.compare_skills(
    resume_skills,
    jd_skills
)

# -------------------------
# ATS Score
# -------------------------
ats_score = analyzer.calculate_ats(
    matched,
    len(jd_skills)
)

# -------------------------
# Resume Rating
# -------------------------
rating = analyzer.resume_rating(ats_score)

# -------------------------
# Recommendations
# -------------------------
recommendations = analyzer.get_recommendations(missing)

# -------------------------
# Display Results
# -------------------------
print("\n========== AI RESUME ANALYZER ==========\n")

print("Matched Skills:")
for skill in matched:
    print("✔", skill)

print("\nMissing Skills:")
for skill in missing:
    print("✘", skill)

print(f"\nATS Score : {ats_score}%")
print("Resume Rating :", rating)

print("\nRecommendations:")
for rec in recommendations:
    print("•", rec)

# -------------------------
# Generate PDF
# -------------------------
generate_report(
    name,
    ats_score,
    matched,
    missing,
    rating,
    recommendations
)

print("\nReport saved successfully in reports/ATS_Report.pdf")