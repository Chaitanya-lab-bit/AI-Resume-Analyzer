import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

def generate_report(name, ats_score, matched, missing, rating, recommendations):

    os.makedirs("reports", exist_ok=True)

    pdf = SimpleDocTemplate("reports/ATS_Report.pdf")
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>AI Resume Analyzer Report</b>", styles["Title"]))
    elements.append(Paragraph(f"<b>Candidate:</b> {name}", styles["Normal"]))
    elements.append(Paragraph(f"<b>ATS Score:</b> {ats_score}%", styles["Normal"]))
    elements.append(Paragraph(f"<b>Resume Rating:</b> {rating}", styles["Normal"]))

    elements.append(Paragraph("<br/><b>Matched Skills</b>", styles["Heading2"]))
    for skill in matched:
        elements.append(Paragraph("✔ " + skill, styles["Normal"]))

    elements.append(Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"]))
    for skill in missing:
        elements.append(Paragraph("✘ " + skill, styles["Normal"]))

    elements.append(Paragraph("<br/><b>Recommendations</b>", styles["Heading2"]))
    for rec in recommendations:
        elements.append(Paragraph("• " + rec, styles["Normal"]))

    pdf.build(elements)

    print("PDF Report Generated Successfully!")