class ResumeAnalyzer:

    def __init__(self):
        self.skills = [
            "Python", "Java", "C", "C++", "SQL",
            "HTML", "CSS", "JavaScript",
            "Flask", "Django",
            "Git", "GitHub",
            "MySQL", "MongoDB",
            "Pandas", "NumPy",
            "AWS", "Docker",
            "REST API"
        ]

    # Extract Skills
    def extract_skills(self, text):

        found_skills = []

        text = text.lower()

        for skill in self.skills:
            if skill.lower() in text:
                found_skills.append(skill)

        return found_skills

    # Compare Skills
    def compare_skills(self, resume_skills, jd_skills):

        matched = []
        missing = []

        for skill in jd_skills:

            if skill in resume_skills:
                matched.append(skill)
            else:
                missing.append(skill)

        return matched, missing

    # Calculate ATS Score
    def calculate_ats(self, matched, total_required):

        if total_required == 0:
            return 0

        score = (len(matched) / total_required) * 100
        return round(score, 2)

    # Resume Rating
    def resume_rating(self, score):

        if score >= 80:
            return "Excellent ⭐⭐⭐⭐⭐"

        elif score >= 60:
            return "Good ⭐⭐⭐⭐"

        elif score >= 40:
            return "Average ⭐⭐⭐"

        else:
            return "Needs Improvement ⭐⭐"

    # Recommendations
    def get_recommendations(self, missing):

        recommendations = {
            "Docker": "Learn Docker for containerization.",
            "AWS": "Learn AWS Cloud Services.",
            "Flask": "Build projects using Flask.",
            "Django": "Learn Django Framework.",
            "REST API": "Practice building REST APIs.",
            "Git": "Improve Git and GitHub skills.",
            "MongoDB": "Practice MongoDB database."
        }

        result = []

        for skill in missing:

            if skill in recommendations:
                result.append(recommendations[skill])
            else:
                result.append(f"Improve your knowledge of {skill}.")

        return result