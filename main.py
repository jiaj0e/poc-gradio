import time
import gradio as gr
from agent import ask
from typing import List


def ask_gemini(message: List[str], history: List[tuple]) -> str:
    msg = "".join(message)
    print("Message:", msg)
    response = ask(msg)
    print("Response:", response)
    time.sleep(0.05)
    history.append((message, response))
    yield response


demo = gr.ChatInterface(
    ask_gemini,
    type="messages",
    flagging_mode="manual",
    flagging_options=["Like", "Spam", "Inappropriate", "Other"],
    save_history=True,
)

if __name__ == "__main__":
    demo.launch()
