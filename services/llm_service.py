import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def ask_llm(prompt: str) -> str:

    try:

        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"LLM Error: {str(e)}"