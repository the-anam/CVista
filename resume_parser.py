import fitz  # PyMuPDF
import docx
import re
from typing import Dict, Any

def extract_text_from_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    return "\n".join(para.text for para in doc.paragraphs)

def parse_resume(text: str) -> Dict[str, Any]:
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    full_text = "\n".join(cleaned_lines)

    name = cleaned_lines[0] if re.match(r"[A-Z][a-z]+ [A-Z][a-z]+", cleaned_lines[0]) else None

    email = re.search(r"[\w\.-]+@[\w\.-]+", full_text)
    phone = re.search(r"\b\d{10}\b|\+91[-\s]?\d{10}", full_text)

    linkedin = re.search(r"(https?://www\.linkedin\.com/in/\S+)", full_text)
    github = re.search(r"(https?://github\.com/\S+)", full_text)

    skill_block = ""
    for i, line in enumerate(cleaned_lines):
        if "Technical Skills" in line or "Programming Languages" in line:
            skill_block = "\n".join(cleaned_lines[i:i+5])
            break

    skills = re.findall(r"Programming Languages\s*:\s*(.*)", skill_block)
    platforms = re.findall(r"Platforms.*?:\s*(.*)", skill_block)
    frameworks = re.findall(r"Frameworks.*?:\s*(.*)", skill_block)
    other_skills = re.findall(r"Other Skills\s*:\s*(.*)", skill_block)

    education = []
    edu_pattern = re.compile(r"Bachelor|Master|High School|B\.Tech|M\.Tech|Ph\.D", re.IGNORECASE)
    for line in cleaned_lines:
        if edu_pattern.search(line):
            education.append(line)

    return {
        "full_name": name,
        "email": email.group(0) if email else None,
        "phone": phone.group(0) if phone else None,
        "linkedin": linkedin.group(1) if linkedin else None,
        "github": github.group(1) if github else None,
        "skills": {
            "programming_languages": skills[0].split(",") if skills else [],
            "platforms": platforms[0].split(",") if platforms else [],
            "frameworks": frameworks[0].split(",") if frameworks else [],
            "other_skills": other_skills[0].split(",") if other_skills else [],
        },
        "education": education
    }

def extract_resume_data(file_path: str) -> Dict[str, Any]:
    if file_path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format")
    return parse_resume(text)
