# src/nderf_xtract/extract_features.py

import requests
import os
import json


API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HF_TOKEN = os.getenv("HF_TOKEN") 

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query_hf(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.status_code)
    print(response.text)
    try:
        return response.json()
    except Exception as e:
        print("Failed to parse JSON:", e)
        return None

def make_prompt(nde_text):
    return (
        "Extract the following features as JSON:\n"
        "- Gender\n"
        "- Date of NDE\n"
        "- Cause\n"
        "- Clinical death (yes/no)\n"
        "- Presence of beings\n"
        "- Out of body experience (yes/no)\n"
        "- Light (yes/no)\n"
        "- Emotional tone\n"
        "- Life review (yes/no)\n"
        "- Any other notable features\n"
        "Account:\n"
        f"{nde_text}\n"
    )

def main():  # sourcery skip: use-named-expression
    data_dir = "data/raw"
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    files = [f for f in os.listdir(data_dir) if f.endswith(".txt")]
    files = sorted(files)[:2]  # Just the first two files

    for filename in files:
        print(f"\nProcessing {filename}...")
        with open(os.path.join(data_dir, filename), "r") as f:
            nde_text = f.read()

        prompt = make_prompt(nde_text)
        result = query_hf({"inputs": prompt})

        if result:
            out_path = os.path.join(output_dir, filename.replace('.txt', '.json'))
            with open(out_path, "w") as out_f:
                json.dump(result, out_f, indent=2)
            print(f"Saved to {out_path}")
        else:
            print(f"Failed to process {filename}")

if __name__ == "__main__":
    main()