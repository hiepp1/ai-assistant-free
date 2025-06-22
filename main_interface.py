import gradio as gr
from chat_gemini import chat_with_gemini, ask_pdf_question

def handle_chat(prompt):
    return chat_with_gemini(prompt)

def handle_pdf(pdf, question):
    if pdf is None or question.strip() == "":
        return "Vui lòng chọn file PDF và nhập câu hỏi."
    return ask_pdf_question(pdf.name, question)

with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Free GEMINI AI ASSISTANT")
    
    with gr.Tab("💬 Chat with Gemini (Flash)"):
        prompt = gr.Textbox(label="Prompt")
        output = gr.Textbox(label="Response")
        submit = gr.Button("Send")
        submit.click(handle_chat, inputs=prompt, outputs=output)

    with gr.Tab("📄 Read & Answer PDF"):
        pdf = gr.File(label="Upload PDF File", file_types=[".pdf"])
        question = gr.Textbox(label="Questions")
        answer = gr.Textbox(label="Answer")
        ask = gr.Button("Ask")
        ask.click(handle_pdf, inputs=[pdf, question], outputs=answer)

demo.launch()
