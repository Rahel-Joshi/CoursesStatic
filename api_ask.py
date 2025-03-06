# api_ask.py
import json
import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from semantic_search_static import semantic_search  # Use the JSON-based KB

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load your free Gemini API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def call_gemini(prompt_text):
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt_text}]
            }
        ]
    }
    try:
        resp = requests.post(
            GEMINI_URL,
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30
        )
        if resp.status_code == 200:
            data = resp.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"Gemini error {resp.status_code}: {resp.text}"
    except Exception as e:
        return f"Error calling Gemini: {str(e)}"

def build_prompt(query, relevant_records):
    system_text = (
        "You are a helpful assistant with detailed knowledge about Caltech courses and option requirements.\n"
        "Use the provided snippets to answer the user's question. If unsure, say you don't have enough info.\n"
    )
    snippet_str = "\n\n".join(
        f"Snippet {i+1}:\n{rec['text']}" for i, rec in enumerate(relevant_records)
    )
    prompt = (
        f"{system_text}\n"
        f"Relevant Info:\n{snippet_str}\n\n"
        f"User Question:\n{query}\n\n"
        f"Answer in plain text:"
    )
    return prompt

@app.route("/api/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        query = data.get("question", "")
        if not query:
            return jsonify({"error": "No question provided."}), 400
        relevant = semantic_search(query, top_n=70)
        if not relevant:
            answer = "No relevant info found in the knowledge base."
        else:
            prompt_text = build_prompt(query, relevant)
            answer = call_gemini(prompt_text)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": "Internal server error.", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)