from PyPDF2 import PdfReader

def read_resume(pdf_path):
    try:
        reader = PdfReader(pdf_path)

        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:
        print("Error:", e)
        return None
    
def read_job_description(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as e:
        print("Error:", e)
        return None
import re

def extract_details(text):

    # Email
    email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    email = email.group() if email else "Not Found"

    # Phone Number
    phone = re.search(r'(\+91\s?)?[6-9]\d{9}', text)
    phone = phone.group() if phone else "Not Found"

    # Name (First line of resume)
    lines = text.split("\n")

    name = "Not Found"

    for line in lines:
        if line.strip():
            name = line.strip()
            break

    return name, email, phone