import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

PROMPT_TEMPLATE = '''
You are an expert resume reviewer. Your task is to provide constructive feedback on the provided resume data.
Please analyze the following aspects:
1. **Clarity and Conciseness:** Is the information easy to understand and free of jargon?
2. **Impact and Achievements:** Does the resume highlight accomplishments with measurable results?
3. **Keywords:** Is it optimized for Applicant Tracking Systems (ATS) with relevant keywords for a [insert target role here, e.g., "Software Engineer"] role?
4. **Formatting and Readability:** Is the layout clean, professional, and easy to read?
5. **Suggestions for Improvement:** Provide specific, actionable advice on how to enhance the resume.

Here is the resume data in JSON format:
<insert resume data>
'''

def get_resume_review(resume_json: dict) -> str:
    # genai.configure(api_key=API_KEY)
    genai.configure(api_key="AIzaSyDzXKj-FX7af4q5c_8oyDP_XlcJE3_SDYk")

    prompt = PROMPT_TEMPLATE.replace("<insert resume data>", str(resume_json))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
