import os
import requests

class Conversation:
    def __init__(self):
        self.history = []
    
    def add_message(self, role, text):
        self.history.append({"role": role, "text": text})
    
    def get_context(self):
        # Construct a conversation context string from the log.
        return "\n".join(f"{msg['role']}: {msg['text']}" for msg in self.history)

def call_gemini_api(conversation, new_user_input):
    conversation.add_message("User", new_user_input)
    prompt = conversation.get_context()
    
    api_url = "https://api.gemini.com/v1/generate"  # Replace with your actual endpoint
    api_key = os.getenv("GEMINI_API_KEY")  # Read the API key from environment variables

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "prompt": prompt,
        "max_tokens": 150  # Adjust as needed
    }
    
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        generated_text = data.get("generated_text", "")
        conversation.add_message("Assistant", generated_text)
        return generated_text
    else:
        print("Error:", response.status_code, response.text)
        return None
