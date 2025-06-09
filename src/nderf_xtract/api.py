import requests
import os

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"  # Example; swap if needed
HF_TOKEN = os.getenv("HF_TOKEN") or "YOUR_HF_TOKEN_HERE"  # Use env var if you want

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query_hf(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

prompt = """
Extract the following fields as JSON:
- Name (if available)
- Gender
- Date of NDE
- Experience Description
...etc

Text:
[PASTE EXPERIENCE TEXT HERE]
"""

result = query_hf({"inputs": prompt})
print(result)