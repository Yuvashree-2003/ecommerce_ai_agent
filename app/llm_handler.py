import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
# ✅ FIXED: updated from v1beta to v1
API_URL  = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"


def get_sql_from_question(question):
    if not API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")

    prompt = f"Translate this question into an SQL query: {question}. Assume tables named ad_sales, total_sales, and eligibility."

    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    params = {"key": API_KEY}

    response = requests.post(API_URL, params=params, json=data)

    try:
        response.raise_for_status()
        response_json = response.json()

        # Debug print to inspect the structure (can be removed in production)
        print("DEBUG Response JSON:", response_json)

        if "candidates" not in response_json:
            raise KeyError("Missing 'candidates' in the response. Full response: " + str(response_json))

        return response_json["candidates"][0]["content"]["parts"][0]["text"]

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")
    except (KeyError, IndexError, TypeError) as e:
        raise ValueError(f"Unexpected response structure: {e}, Response: {response.text}")
