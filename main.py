import os
import sys
from resume_parser import extract_resume_data
from gemini_client import get_resume_review
from utils import save_review

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <resume_file.pdf|docx>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    print("Extracting and parsing resume...")
    resume_data = extract_resume_data(file_path)
    print("Parsed resume data:")
    print(resume_data)

    print("\nSending to Gemini for review...")
    review = get_resume_review(resume_data)
    print("\nGemini Resume Review:\n")
    print(review)

    out_file = "review.json" if review.strip().startswith("{") else "review.txt"
    save_review(review, out_file)
    print(f"\nReview saved to {out_file}")

if __name__ == "__main__":
    main()
