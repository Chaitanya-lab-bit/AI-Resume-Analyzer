from parser import read_resume, read_job_description, extract_details
from analyzer import (
    extract_skills,
    compare_skills,
    calculate_ats,
    resume_rating,
    get_recommendations
)
from report import generate_report

# File paths
resume_path = "resumes/resume.pdf"
job_path = "job_descriptions/job_descriptions.txt"

# Read files
resume_text = read_resume(resume_path)
job_text = read_job_description(job_path)

# Check if files are read successfully
if resume_text is None or job_text is None:
    print("Error reading files.")
    exit()

# Extract candidate details
name, email, phone = extract_details(resume_text)

# Extract skills
resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(job_text)

# Compare skills
matched, missing = compare_skills(resume_skills, jd_skills)

# Calculate ATS score
ats_score = calculate_ats(matched, len(jd_skills))

# Resume rating
rating = resume_rating(ats_score)

# Recommendations
recommendations = get_recommendations(missing)

# Display Results
print("\n========== AI RESUME ANALYZER ==========\n")

print("Candidate Details")
print("-----------------------------")
print("Name :", name)
print("Email:", email)
print("Phone:", phone)

print("\nResume Skills")
print("-----------------------------")
print(resume_skills)

print("\nJob Description Skills")
print("-----------------------------")
print(jd_skills)

print("\nMatched Skills")
print("-----------------------------")
print(matched)

print("\nMissing Skills")
print("-----------------------------")
print(missing)

print(f"\nATS Score : {ats_score}%")
print("Resume Rating :", rating)

print("\nRecommendations")
print("-----------------------------")
for rec in recommendations:
    print("•", rec)

# Generate PDF Report
generate_report(
    name,
    ats_score,
    matched,
    missing,
    rating,
    recommendations
)

print("\n✅ PDF Report Generated Successfully!")
print("Saved in: reports/ATS_Report.pdf")