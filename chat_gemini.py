import os
import google.generativeai as genai
from dotenv import load_dotenv
import fitz

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def chat_with_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

def extract_text_from_pdf(pdf_path):
    doc=fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()

    doc.close()
    return text

def ask_pdf_question(pdf_path, user_question):
    pdf_text = extract_text_from_pdf(pdf_path)
    prompt = f"""Below is the content of PDF :\n\n{pdf_text}n\nWith given content, answer these questions:\n{user_question}"""

    response = model.generate_content(prompt)
    return response.text