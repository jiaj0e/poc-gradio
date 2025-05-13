# from google import genai
import os
import requests
import json
from models import GenAiResponse

API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    raise KeyError("API_KEY not found. Please set the API_KEY environment variable.")

MODEL = "gemini-2.0-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"


# FIXME: idk why is not working (maybe python version)
# client = genai.Client(api_key="YOUR_API_KEY")
# print("API KE   Y:", API_KEY)

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="Explain how AI works in a few words",
# )


def ask(message: str) -> str:
    """
    Ask the model a question and return the answer.
    """
    data = {
        "contents": [
            {
                "parts": [{"text": message}],
            }
        ]
    }
    response = requests.post(URL, headers={"Content-Type": "application/json"}, data=json.dumps(data))
    if response.status_code == 200:
        try:
            response_obj = GenAiResponse(**response.json())
            return response_obj.candidates[0].content.parts[0].text
        except Exception as e:
            print("Error:", e)
            return "I'm sorry, I couldn't process your request."
    else:
        print("Error: " + response.text)
        return "I'm sorry, I couldn't process your request."
