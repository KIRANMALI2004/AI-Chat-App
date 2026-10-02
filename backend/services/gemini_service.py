import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(prompt, context=""):
    final_prompt = prompt

    if context:
        final_prompt = f"""
Use the following uploaded document to answer the question.

DOCUMENT:

{context}

QUESTION:

{prompt}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=final_prompt,
    )

    return response.text