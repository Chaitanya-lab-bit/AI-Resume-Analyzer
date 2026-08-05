import os

file_path = "resumes/resume.pdf"

print("Exists:", os.path.exists(file_path))
print("Size:", os.path.getsize(file_path), "bytes")

with open(file_path, "rb") as f:
    first_bytes = f.read(10)

print("First 10 bytes:", first_bytes)