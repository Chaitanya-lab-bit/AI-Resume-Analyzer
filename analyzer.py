def extract_skills(text):
    # List of skills to search
    skills = [
        "Python", "Java", "C", "C++", "SQL",
        "HTML", "CSS", "JavaScript",
        "Django", "Flask",
        "Git", "GitHub",
        "MySQL", "MongoDB",
        "AWS", "Docker",
        "REST API", "Pandas",
        "NumPy", "Scikit-learn",
        "TensorFlow", "OpenCV"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills


def compare_skills(resume_skills, jd_skills):

    matched = []
    missing = []

    for skill in jd_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing


def calculate_ats(matched, total_required):

    if total_required == 0:
        return 0

    score = (len(matched) / total_required) * 100

    return round(score, 2)

def resume_rating(score):

    if score >= 80:
        return "Excellent ⭐⭐⭐⭐⭐"

    elif score >= 60:
        return "Good ⭐⭐⭐⭐"

    elif score >= 40:
        return "Average ⭐⭐⭐"

    else:
        return "Needs Improvement ⭐⭐"

def get_recommendations(missing):

    recommendations = {
        "Docker": "Learn Docker for containerization.",
        "AWS": "Gain experience with AWS cloud services.",
        "REST API": "Build REST APIs using Flask or Django.",
        "Flask": "Learn Flask and build small projects.",
        "Git": "Practice Git and GitHub."
    }

    result = []

    for skill in missing:
        if skill in recommendations:
            result.append(recommendations[skill])
        else:
            result.append(f"Improve your knowledge of {skill}.")

    return result