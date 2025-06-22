import gradio as gr
from chat_gemini import chat_with_gemini

iface = gr.Interface(
    fn = chat_with_gemini,
    inputs = gr.Textbox(lines=4, placeholder="Input question..."),
    outputs="text",
    title="Chat with Gemini",
)

iface.launch()