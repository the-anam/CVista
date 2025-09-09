📄 CVista – Resume Checker using Google Gemini API
CVista is an AI-powered Resume Checker built with Python, using Google Gemini API for intelligence, Flask as the backend framework, and Streamlit for a clean and interactive frontend UI.
This tool helps users upload their resumes and receive intelligent feedback and analysis based on job descriptions, formatting guidelines, and best practices — making it ideal for job seekers looking to polish their CVs.

🚀 Features
✅ Resume Parsing: Extracts relevant information (skills, education, experience, etc.) from uploaded resumes.

🧠 AI-Powered Feedback: Utilizes Google Gemini API to give smart, contextual suggestions based on industry best practices.

📄 JD Comparison: Compares your resume with a Job Description (JD) to assess relevancy and highlight skill gaps.

🌐 Web-Based UI: Built with Streamlit for a responsive and easy-to-use user interface.

🔧 Flask Backend: Handles resume parsing and Gemini API communication securely and efficiently.

🔐 Environment Variables: Sensitive data (API keys, config) handled via .env file.

🧠 How it Works
Upload Resume: Users can upload their CV in PDF format via the Streamlit UI.
Parse Resume: The resume is parsed using Python to extract important sections like:
Contact Info
Education
Skills
Experience

Enter Job Description: Users paste or upload a job description they are targeting.
AI Evaluation:
The parsed resume and JD are sent to the Google Gemini API.
Gemini compares the two and provides:
Skills matching
Experience relevance

Suggestions for improvement
Result Display: The feedback is rendered in the Streamlit UI with clear formatting.

🗂️ Project Structure
CVista/
│
├── app.py               # Flask backend to handle API routes
├── main.py              # Streamlit UI logic
├── gemini_client.py     # Handles communication with Google Gemini API
├── resume_parser.py     # Extracts data from resumes
├── utils.py             # Helper functions
├── .env                 # Environment variables (API keys, config)
├── temp/                # Temporary storage for uploaded files
└── __pycache__/         # Python cache
🧪 Tech Stack
Technology	Role
Python	Core language for backend & parsing
Google Gemini	AI feedback engine
Flask	API backend
Streamlit	Frontend interface
PyPDF2 / pdfplumber	Resume text extraction
dotenv	Environment variable management
⚙️ Installation
Clone the repo

git clone https://github.com/the-anam/CVista.git
cd CVista
Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
Set up .env file

Create a .env file in the root directory and add your Gemini API key:

GEMINI_API_KEY=your_google_gemini_api_key
Run the Streamlit App

streamlit run main.py
📸 Demo
You can add screenshots or a demo video link here.

📌 To-Do (Future Enhancements)
 Add support for DOCX format

 User authentication (Flask-Login)

 Resume score / rating system

 Save feedback history for users

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

