import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def call_ai(user_input, products):
    url = "https://openrouter.ai/api/v1/chat/completions"

    prompt = f"""
You are a STRICT AI shopping assistant for a baby/mother store.

User request:
{user_input}

Available products:
{products}

STRICT RULES (VERY IMPORTANT):
- Only recommend products relevant to babies, mothers, or children
- If the request is unrelated (e.g., jewelry, girlfriend gifts, electronics), DO NOT recommend anything
- In that case, return EXACTLY:
{{"error": "Out of scope request"}}

- Only use products from the provided list
- Stay within the user's budget if mentioned
- Do NOT hallucinate or assume
- If no valid product exists, return:
{{"error": "No suitable products found"}}

Output must be STRICT JSON only (no extra text):

{{
  "recommendations": [
    {{
      "name": "string",
      "price": number,
      "reason": "short explanation",
      "arabic_name": "arabic translation"
    }}
  ]
}}
"""

    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "You must strictly follow instructions and never hallucinate."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.2   # 🔥 lower = less hallucination
        }
    )

    return response.json()