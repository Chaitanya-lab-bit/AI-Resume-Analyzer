import pdfplumber
import re


class ResumeParser:

    def __init__(self):
        pass

    # Read Resume PDF
    def read_resume(self, pdf_path):

        try:
            text = ""

            with pdfplumber.open(pdf_path) as pdf:

                for page in pdf.pages:
                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

            return text

        except Exception as e:
            print("Error:", e)
            return None

    # Read Job Description Text File
    def read_job_description(self, file_path):

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()

        except Exception as e:
            print("Error:", e)
            return None

    # Extract Name, Email and Phone
    def extract_details(self, text):

        # Email
        email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
        email = email_match.group() if email_match else "Not Found"

        # Phone
        phone_match = re.search(r'(\+91\s?)?[6-9]\d{9}', text)
        phone = phone_match.group() if phone_match else "Not Found"

        # Name (First non-empty line)
        name = "Not Found"

        for line in text.split("\n"):
            if line.strip():
                name = line.strip()
                break

        return name, email, phone