# from google import genai
import os

# import requests
# import json
# from reflex_app.models import GenAiResponse
from google import genai
import asyncio  # Import asyncio for async functionality
# from reflex_app.style import api_error_style, api_success_style  # Import centralized styles

API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    raise KeyError("API_KEY not found. Please set the API_KEY environment variable.")

MODEL = "gemini-2.0-flash"
# URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
try:
    AI = genai.Client(api_key=API_KEY)
except Exception as e:
    print("Error initializing GenAI client:", e)
    raise


async def ask(message: str):
    """
    Ask the model a question and yield the answer chunks asynchronously.
    """
    try:
        response = AI.models.generate_content_stream(
            model=MODEL,
            contents=message,
        )
        for chunk in response:  # Iterate over the generator
            yield chunk.text  # Yield each chunk of text
    except Exception as e:
        print("Error:", e)
        yield "I'm sorry, I couldn't process your request."


# Example usage
if __name__ == "__main__":

    async def main():
        async for chunk in ask("What is the meaning of life?"):
            print(chunk, end="")

    asyncio.run(main())
